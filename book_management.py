"""Consider a scenario where you are developing a software application 
for a library management system using Python. You have identified the 
need for creating classes to represent books and library members. 
Design and implement the necessary classes using object-oriented 
programming concepts.
1.Create a class named "Book" with the following attributes and 
methods: 
Attributes:
1. title: a string representing the title of the book.
2. author: a string representing the author of the book.
3. publication_year: an integer representing the year of publication.
4. borrowed: a boolean indicating whether the book is currently borrowed or 
not.
Methods:
1. borrow_book(): a method that sets the "borrowed" attribute to True, 
indicating that the book has been borrowed.
2. return_book(): a method that sets the "borrowed" attribute to False, 
indicating that the book has been returned.
3. display_info(): a method that displays the title, author, publication year, and 
borrowed status of the book."""
class Book:
    # Initialize book attributes
    def __init__(self, title, author, publication_year, borrowed=False):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = borrowed  # Allows setting borrowed status when creating a book

    # Method to mark the book as borrowed
    def borrow_book(self):
        self.borrowed = True

    # Method to mark the book as returned
    def return_book(self):
        self.borrowed = False

    # Method to display book information
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print("Borrowed:", self.borrowed)
