from pymongo import MongoClient
from scholars import ScholarsHaven
from datetime import datetime

def main():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["university_database"]
    
    # Get the scholars data
    scholars_haven = ScholarsHaven(db)
    
    """
    1.	Add a new book to the library (title, author, genre, ISBN, and quantity).
    """
    scholars_haven.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", "1", 50)
    scholars_haven.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction", "2", 40)
    scholars_haven.add_book("1984", "George Orwell", "Dystopian", "3", 30)
    scholars_haven.add_book("Pride and Prejudice", "Jane Austen", "Romance", "4", 35)
    scholars_haven.add_book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "Non-Fiction", "5", 25)
    scholars_haven.add_book("The Catcher in the Rye", "J.D. Salinger", "Fiction", "6", 45)
    scholars_haven.add_book("Becoming", "Michelle Obama", "Biography", "7", 20)
    scholars_haven.add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", "8", 60)
    scholars_haven.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Fantasy", "9", 75)
    scholars_haven.add_book("The Art of War", "Sun Tzu", "Philosophy", "10", 15)
    
    # Display the books
    print("#" * 80)
    print("List All The Books Available")
    print("#" * 80)
    scholars_haven.display_books()
    
    
    """
    2.    Check if a book is available for borrowing by its ISBN.
    """
    print("#" * 80)
    print("Check if a book is available for borrowing by its ISBN:")
    print("#" * 80)
    scholars_haven.if_book_available(ISBN= '1')
    
    """
    3.	Allow a member to borrow a book (member_id, ISBN, borrow_date, return_date).
    """
    from datetime import datetime

    scholars_haven.borrow_book(member_id=1, ISBN='1', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=1, ISBN='2', borrow_date=datetime(2024, 12, 6, 4, 0, 0), return_date=datetime(2024, 12, 7, 4, 0, 0))
    scholars_haven.borrow_book(member_id=1, ISBN='2', borrow_date=datetime(2024, 11, 7, 4, 0, 0), return_date=datetime(2024, 11, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=1, ISBN='2', borrow_date=datetime(2024, 12, 6, 4, 0, 0), return_date=datetime(2024, 12, 7, 4, 0, 0))
    scholars_haven.borrow_book(member_id=1, ISBN='3', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=2, ISBN='2', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=3, ISBN='3', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=4, ISBN='4', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=5, ISBN='5', borrow_date=datetime(2024, 12, 7, 4, 0, 0), return_date=datetime(2024, 12, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=5, ISBN='5', borrow_date=datetime(2024, 11, 7, 4, 0, 0), return_date=datetime(2024, 11, 10, 4, 0, 0))
    scholars_haven.borrow_book(member_id=5, ISBN='2', borrow_date=datetime(2024, 12, 4, 4, 0, 0), return_date=datetime(2024, 12, 5, 4, 0, 0))
    scholars_haven.borrow_book(member_id=5, ISBN='3', borrow_date=datetime(2024, 12, 4, 4, 0, 0), return_date=datetime(2024, 12, 5, 4, 0, 0))
    scholars_haven.borrow_book(member_id=5, ISBN='4', borrow_date=datetime(2024, 12, 4, 4, 0, 0), return_date=datetime(2024, 12, 5, 4, 0, 0))

    
    
    """ 
    4.	List all books currently borrowed by a specific member (member_id).
    """
    print("#" * 80)
    print("List all books currently borrowed by member with ID 1:")
    print("#" * 80)
    scholars_haven.display_borrowed_books(member_id=1)
    
    
    
    """ 
    5.	Add a new member to the library (name, email, phone, and membership_date).
    """
    scholars_haven.add_member(member_id = 1,name = "John Doe", email = "john.doe@example.com", phone = "123-456-7890", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 2,name = "Jane Smith", email = "jane.smith@example.com", phone = "987-654-3210", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 3,name = "Bob Johnson", email = "bob.johnson@example.com", phone = "789-456-1230", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 4,name = "Alice Johnson", email = "alice.johnson@example.com", phone = "456-789-0123", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 5, name = "David Wilson", email = "david.wilson@example.com", phone = "321-654-9870", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 6, name = "Emily Davis", email = "emily.davis@example.com", phone = "210-345-6789", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 7, name = "Michael Lee", email = "michael.lee@example.com", phone = "109-876-5432", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 8, name = "Sarah Brown", email = "sarah.brown@example.com", phone = "987-654-3210", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 9, name = "David Garcia", email = "david.garcia@example.com", phone = "654-321-9870", membership_date = datetime(2024,12, 1, 4, 0, 0))
    scholars_haven.add_member(member_id = 10, name = "Jessica Taylor", email = "jessica.taylor@example.com", phone = "543-210-9876", membership_date = datetime(2024,12, 1, 4, 0, 0))
    
    
    
    print("#" * 80)
    print("List all members:")
    print("#" * 80)
    scholars_haven.display_members()
    
    
              
    """ 
    6.	List all members who borrowed books in a given month.
    """     
    print("#" * 80)
    print("List all members who borrowed books in a given month: Month 12")
    print("#" * 80)
    scholars_haven.display_members_borrowed_books_in_month(month=12)
    

    """ 
    7.	Record the return of a borrowed book and update its quantity.
    """
    print("#" * 80)
    print("List all books returned:")
    print("#" * 80)
    scholars_haven.return_book(ISBN= '2', member_id=1)
    scholars_haven.return_book(ISBN= '5', member_id=5)
    
    """ 
    8.	List the most borrowed books, ordered by borrowing frequency.
    """
    print("#" * 80)
    print("List the most borrowed books:")
    print("#" * 80)
    scholars_haven.display_most_borrowed_books()
    
    
    """
    9.	Identify members with overdue books.
    """
    print("#" * 80)
    print("List members with overdue books:")
    print("#" * 80)
    scholars_haven.members_with_overdue_books()
    


    """
    10.    Recommend books to members based on genres of books they’ve previously borrowed.
    """
    print("#" * 80)
    print("Recommend books to members:")
    print("#" * 80)
    scholars_haven.recommend_books(member_id=1)
    # scholars_haven.recommend_books(member_id=5)

    
    
    

    
    
    
if __name__ == "__main__":
    main()