"""1.Create a class named "LibraryMember" with the following attributes and 
methods: 
Attributes:
1. member_id: an integer representing the unique identifier of the library 
member.
2. name: a string representing the name of the library member.
3. borrowed_books: a list of Book objects representing the books currently 
borrowed by the member.
Methods:
1. borrow_book(book): a method that takes a Book object as input and adds it to 
the "borrowed_books" list.
2. return_book(book): a method that takes a Book object as input and removes it 
from the "borrowed_books" list.
3. display_info(): a method that displays the member ID, name, and the list of 
borrowed books.
1.Implement appropriate inheritance between the classes to represent 
the relationship between books and library members."""
# Step 1: Create a class named "LibraryMember" with the required attributes and methods.
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id  # Unique ID for the member
        self.name = name  # Name of the member
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        """Adds a Book object to the borrowed_books list."""
        self.borrowed_books.append(book)

    def return_book(self, book):
        """Removes a Book object from the borrowed_books list if it exists."""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("This book was not borrowed by the member.")

    def display_info(self):
        """Displays the member's ID, name, and list of borrowed books."""
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print("-", book.title, "by", book.author)


# Step 2: Implement inheritance to represent the relationship between books and library members.
class Book:
    def __init__(self, title, author):
        self.title = title  # Title of the book
        self.author = author  # Author of the book