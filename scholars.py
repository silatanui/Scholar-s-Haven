from datetime import datetime

class ScholarsHaven:
    def __init__(self, db):
        self.db = db
    
    """
    1. Add a new book to the library (title, author, genre, ISBN, and quantity).
    """
    def if_book_added(self, ISBN):
        result = self.db.book.find_one({"ISBN": ISBN})
        return result is not None
    
    def add_book(self, title, author, genre, ISBN, quantity):
        if self.if_book_added(ISBN):
            print("Book already exists.")
            return False
        
        book = {
            "title": title,
            "author": author,
            "genre": genre,
            "ISBN": ISBN,
            "quantity": quantity,
        }
        self.db.book.insert_one(book)
        print(f"Book '{title}' added successfully.")
        return True

    def display_books(self):
        books = self.db.book.find({}, {"_id": False})
        for book in books:
            print(f"ISBN: {book['ISBN']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Quantity: {book['quantity']}")
            print("-" * 80)
    
    """
    2. Check if a book is available for borrowing by its ISBN.
    """
    def if_book_available(self, ISBN):
        result = self.db.book.find_one({"ISBN": ISBN, "quantity": {"$gt": 0}})
        if result:
            title = result["title"]
            quantity = result["quantity"]
            print(f"The book '{title}' is available for borrowing. Quantity: {quantity}")
            return True
        else:
            print("The book is not available for borrowing.")
            return False
        

    """
    3. Allow a member to borrow a book.
    """
    def has_member_borrowed(self, member_id, ISBN):
        result = self.db.borrowed_books.find_one({"member_id": member_id, "ISBN": ISBN})
        return result is not None

    def borrow_book(self, member_id, ISBN, borrow_date, return_date):
        if not self.if_book_available(ISBN):
            print(f"Cannot borrow book with ISBN: {ISBN}.")
            return False
        
        if self.has_member_borrowed(member_id, ISBN):
            print(f"Member {member_id} has already borrowed the book with ISBN: {ISBN}.")
            return False

        # Reduce book quantity by 1
        self.db.book.update_one({"ISBN": ISBN}, {"$inc": {"quantity": -1}})
        
        # Record borrowing
        self.db.borrowed_books.insert_one({
            "member_id": member_id,
            "ISBN": ISBN,
            "borrow_date": borrow_date,
            "return_date": return_date,
        })
        print(f"Book with ISBN {ISBN} borrowed successfully by member {member_id}.")
        return True

    """
    4. List all books currently borrowed by a specific member.
    """
    def display_borrowed_books(self, member_id):
        borrowed_books = self.db.borrowed_books.find({"member_id": member_id})
        if borrowed_books is None:
            print(f"No books borrowed by member {member_id}.")
        else:
            for record in borrowed_books:
                print(f"ISBN: {record['ISBN']}")
                print(f"Borrow Date: {record['borrow_date']}")
                print(f"Return Date: {record['return_date']}")
                print("-" * 80)

          
    """
    5. Add a new member to the library (name, email, phone, and membership_date).
    """
    def is_member_added(self, member_id):
        result = self.db.members.find_one({'member_id': member_id})
        return result is not None

    def add_member(self, member_id, name, email, phone, membership_date):
        if self.is_member_added(member_id):
            print(f"Member with member_id {member_id} already exists.")
            return False
        
        member = {
            'member_id': member_id,
            "name": name,
            "email": email,
            "phone": phone,
            "membership_date": membership_date,
        }
        self.db.members.insert_one(member)
        print(f"Member '{name}' added successfully.")
        return True


    # Display All the members
    def display_members(self):
        members = self.db.members.find({}, {"_id": False})
        for member in members:
            print(f"Name: {member['name']}")
            print(f"Email: {member['email']}")
            print(f"Phone: {member['phone']}")
            print(f"Membership Date: {member['membership_date']}")
            print("-" * 80)
            
    """ 
    6.	List all members who borrowed books in a given month.
    """      
    def display_members_borrowed_books_in_month(self, month):
        # Defining the range for december
        start_date = datetime(2024, month, 1, 0, 0)
        end_date = datetime(2024, month, 30, 0, 0)
        borrowed_books = self.db.borrowed_books.find({"borrow_date": {
            "$gte": start_date,
            "$lte": end_date,
        }})
        for book in borrowed_books:
            member_id = book['member_id']
            member_details = self.db.members.find({'member_id': member_id})
            for member in member_details:
                print(f"Member: {member['name']}")
                print(f"Email: {member['email']}")
                print(f"Phone: {member['phone']}")
                print(f"Member ID: {member['member_id']}")
                print(f"ISBN: {book['ISBN']}")
                print(f"Borrow Date: {book['borrow_date']}")
                print(f"Return Date: {book['return_date']}")
                print("-" * 80)
                
    
    """
    7.    Record the return of a borrowed book and update its quantity.
    """
    def return_book(self, member_id, ISBN):
        borrowed_book = self.db.borrowed_books.find_one({"member_id": member_id, "ISBN": ISBN})
        if borrowed_book is None:
            print(f"Member {member_id} has not borrowed the book with ISBN: {ISBN}.")
            return False
        
        # Calculate the return date
        borrow_date = borrowed_book["borrow_date"]
        # return_date = borrow_date + timedelta(days=30)
        
        # Update the book quantity
        self.db.book.update_one({"ISBN": ISBN}, {"$inc": {"quantity": 1}})
        
        # Delete the borrowed book record
        self.db.borrowed_books.delete_one({"member_id": member_id, "ISBN": ISBN})
        
        
        print(f"Book with ISBN {ISBN} returned successfully by member {member_id}.")
        return True
    
    """
    8.    List the most borrowed books, ordered by borrowing frequency.
    """
    def display_most_borrowed_books(self):
        pipeline = [
            {
                '$group': {
                    '_id': '$ISBN', 
                    'NumberofBooks': {
                        '$sum': 1
                    }
                }
            }, {
                '$sort': {
                    'NumberofBooks': -1
                }
            }
        ]
        result = self.db.borrowed_books.aggregate(pipeline)
        for book in result:
            print(f"ISBN: {book['_id']}")
            # Get the book name:
            ISBN = book['_id']
            book_details = self.db.book.find_one({'ISBN': ISBN})
            print(f"Title: {book_details['title']}")
            print(f"Number of Borrowings: {book['NumberofBooks']}")
            print("-" * 80)
            
    """
    9.	Identify members with overdue books.
    """
    def members_with_overdue_books(self):
        # Identify members with overdue books
        pipeline = [
            {
                '$match': {
                    'return_date': {
                        '$lte': datetime.now()
                    }
                }
            }, {
                '$lookup': {
                    'from': 'members', 
                    'localField': 'member_id', 
                    'foreignField': 'member_id', 
                    'as': 'members'
                }
            }, {
                '$unwind': '$members'
            }
        ]
        result = self.db.borrowed_books.aggregate(pipeline)
        for book in result:
            print(f"Member: {book['members']['name']}")
            print(f"Email: {book['members']['email']}")
            print(f"Phone: {book['members']['phone']}")
            print(f"Member ID: {book['members']['member_id']}")
            print(f"ISBN: {book['ISBN']}")
            print(f"Borrow Date: {book['borrow_date']}")
            print(f"Return Date: {book['return_date']}")
            print("-" * 80)
            
    def recommend_books(self, member_id):
        # Get the books borrowed by the member
        borrowed_books = self.db.borrowed_books.find({"member_id": member_id})
        
        # Get the genres of the books borrowed by the member
        genres = []
        for book in borrowed_books:
            ISBN = book['ISBN']
            book_details = self.db.book.find_one({'ISBN': ISBN})
            if book_details and 'genre' in book_details:
                genres.append(book_details['genre'])
        
        if not genres:
            print("No borrowed books found for this member.")
            return []
        
        # Eliminate duplicates in genres
        genres = list(set(genres))
        
        # Define an aggregation pipeline to get recommended books
        pipeline = [
            {
                '$match': {
                    'genre': {'$in': genres},  # Match books in similar genres
                    'quantity': {'$gt': 0}    # Ensure books are available
                }
            }, {
                '$sort': {
                    'quantity': -1  # Sort by quantity (popularity/availability)
                }
            }, {
                '$project': {
                    '_id': 0,
                    'title': 1,
                    'ISBN': 1,
                    'genre': 1,
                    'quantity': 1
                }
            }, {
                '$limit': 5  # Limit to top 5 recommendations
            }
        ]
        
        # Execute the aggregation pipeline
        recommended_books = list(self.db.book.aggregate(pipeline))
        
        # Output recommendations
        if recommended_books:
            for book in recommended_books:
                print(f"Title: {book['title']}, ISBN: {book['ISBN']}, Genre: {book['genre']}")
        else:
            print("No recommendations found.")
        
        return recommended_books

            
        
"""
The Scholar's Haven is a bustling library known for its diverse collection of books and dedicated members. To modernize its operations, the library is transitioning to a digital database system to manage books, members, and activities efficiently. Your task is to develop and optimize this system.
Tasks:
1.	Add a new book to the library (title, author, genre, ISBN, and quantity).
2.	Check if a book is available for borrowing by its ISBN.
3.	Allow a member to borrow a book (member_id, ISBN, borrow_date, return_date).
4.	List all books currently borrowed by a specific member (member_id).
5.	Add a new member to the library (name, email, phone, and membership_date).
6.	List all members who borrowed books in a given month.
7.	Record the return of a borrowed book and update its quantity.
8.	List the most borrowed books, ordered by borrowing frequency.
9.	Identify members with overdue books.
10.	Recommend books to members based on genres of books they’ve previously borrowed.
"""