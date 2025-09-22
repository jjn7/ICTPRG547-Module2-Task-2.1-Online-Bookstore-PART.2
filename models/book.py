class Book:
    # __init__ is the constructor - runs when we create a new book
    # self refers to the specific book object being created
    def __init__(self, book_id, title, author, genre, price, in_stock=True):
        # Store the data passed in as properties of this book object
        self.id = book_id           # Unique identifier
        self.title = title
        self.author = author        
        self.genre = genre
        self.price = price
        self.in_stock = in_stock    #defaults to True
    
    # __str__ defines what happens when we print() a book object
    def __str__(self):
        # Return a formatted string showing key book info
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}"
    
    # __repr__ is similar to __str__ but for debugging/development
    def __repr__(self):
        return self.__str__()  # Just use the same format as __str__