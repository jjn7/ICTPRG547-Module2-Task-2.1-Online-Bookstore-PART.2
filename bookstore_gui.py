# Basic GUI Window for Bookstore Application

# Import tkinter - Python's built-in GUI library
import tkinter as tk

# Import my classes from Part 1
from models.book import Book
from data_structures.linked_list import DoubleLinkedList
from data_structures.hash_table import HashTable
from data_structures.binary_tree import BinaryTree

class BookstoreGUI:
    """
    Main class for my bookstore GUI application
    """

    def __init__(self):
        """
        Constructor - sets up the basic window and data structures
        This runs when I create a new BookstoreGUI object
        """

        # Create the main window using tkinter
        self.root = tk.Tk()

        # Set the window title (appears in title bar)
        self.root.title("Online Bookstore Inventory System")

        # Set the window size (width x height in pixels)
        self.root.geometry("800x600")

        # Initialize data structures from Part 1
        # These are the same structures I used in main.py
        self.inventory = DoubleLinkedList()  # For storing books in order
        self.quick_lookup = HashTable()      # For fast ID-based searches
        self.tree_lookup = BinaryTree()      # For alphabetical sorting/searching

        # Add some sample books so I have data to work with
        self.load_sample_books()

        # Add basic labels - no styling yet
        welcome_label = tk.Label(self.root, text="Bookstore Inventory System")
        welcome_label.pack()

        # Show book count to confirm data structures work
        book_count_label = tk.Label(self.root, text=f"Books loaded: {self.inventory.size}")
        book_count_label.pack()

        # Add one simple button to view books
        view_button = tk.Button(self.root, text="View Books", command=self.view_books)
        view_button.pack()

        # Add basic text area to display book information
        self.text_area = tk.Text(self.root, height=15, width=60)
        self.text_area.pack()
        
        # Add the new Add Book frame after creating the text area
        self.create_add_book_frame()

    def load_sample_books(self):
        """
        Loads some sample books into the data structures
        This provides data to work with for testing the GUI
        """

        # Create sample books (same ones from main.py for consistency)
        sample_books = [
            Book(12345, "Harry Potter", "J.K. Rowling", "Fantasy", 29.99),
            Book(67890, "Animal Farm", "George Orwell", "Fiction", 19.99),
            Book(23456, "The Great Gatsby", "F. Scott Fitzgerald", "Historical Fiction", 24.99)
        ]

        # Add each book to all data structures
        for book in sample_books:
            # Add to linked list (maintains insertion order)
            self.inventory.add_book(book)

            # Add to hash table (fast ID lookup)
            self.quick_lookup.add_book(book)

            # Add to binary tree (alphabetical sorting)
            self.tree_lookup.add_book(book)

    def view_books(self):
        """
        Display all books from the linked list in the text area
        This is called when the View Books button is clicked
        """
        # Clear the text area first
        self.text_area.delete(1.0, tk.END)

        # Check if there are any books
        if self.inventory.size == 0:
            self.text_area.insert(tk.END, "No books in inventory")
            return

        # Display books from linked list (maintains insertion order)
        self.text_area.insert(tk.END, "Books in Inventory:\n\n")

        current_node = self.inventory.head
        book_number = 1

        while current_node is not None:
            book = current_node.data
            # Display basic book information
            book_info = f"{book_number}. {book}\n"
            book_info += f"   Genre: {book.genre}, Price: ${book.price}\n\n"

            self.text_area.insert(tk.END, book_info)

            current_node = current_node.next
            book_number += 1

    def create_add_book_frame(self):
        """
        Create a frame with input fields for adding a new book
        grid layout used to organize the input fields neatly
        """
        
        # LabelFrame creates a bordered box with a title
        add_frame = tk.LabelFrame(self.root, text="Add New Book", padx=10, pady=10)
        
        # pack() places the frame on the window
        # fill="x" makes it stretch horizontally
        add_frame.pack(padx=10, pady=10, fill="x")
        
        # Using grid layout to arrange input fields in rows and columns
        
        # ROW 0: Book ID and Title
        tk.Label(add_frame, text="Book ID:").grid(row=0, column=0, sticky="w")
        
        # References to Entry widgets to get their values later
        self.id_entry = tk.Entry(add_frame, width=15)
        self.id_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(add_frame, text="Title:").grid(row=0, column=2, sticky="w")
        self.title_entry = tk.Entry(add_frame, width=30)
        self.title_entry.grid(row=0, column=3, padx=5)
        
        # ROW 1: Author and Genre
        tk.Label(add_frame, text="Author:").grid(row=1, column=0, sticky="w")
        self.author_entry = tk.Entry(add_frame, width=30)
        self.author_entry.grid(row=1, column=1, padx=5)
        
        tk.Label(add_frame, text="Genre:").grid(row=1, column=2, sticky="w")
        self.genre_entry = tk.Entry(add_frame, width=20)
        self.genre_entry.grid(row=1, column=3, padx=5)
        
        # ROW 2: Price and Add Button
        tk.Label(add_frame, text="Price:").grid(row=2, column=0, sticky="w")
        self.price_entry = tk.Entry(add_frame, width=10)
        self.price_entry.grid(row=2, column=1, padx=5)
        
        # Button that calls add_book method when clicked
        add_button = tk.Button(add_frame, text="Add Book", command=self.add_book, 
                              bg="green", fg="white")
        add_button.grid(row=2, column=3, padx=5, pady=5)

    def add_book(self):
        """
        Add a new book to all data structures
        This handles getting input, validating it, and updating everything
        """
        
        # Using try/except to handle potential errors (like invalid numbers)
        try:
            # Get values from my input fields
            book_id = int(self.id_entry.get())
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()
            genre = self.genre_entry.get().strip()
            price = float(self.price_entry.get())
            
            # Validate that all fields are filled
            if not title or not author or not genre:
                self.show_message("Error", "Please fill in all fields")
                return
            
            # Check price is valid
            if price < 0:
                self.show_message("Error", "Price cannot be negative")
                return
            
            # Check if book ID already exists using my hash table
            if self.quick_lookup.search_book(book_id):
                self.show_message("Error", f"Book with ID {book_id} already exists")
                return
            
            # Create new book object
            new_book = Book(book_id, title, author, genre, price)
            
            # Add to all three data structures
            self.inventory.add_book(new_book)
            self.quick_lookup.add_book(new_book)
            self.tree_lookup.add_book(new_book)
            
            # Update the GUI
            self.clear_entries()
            self.view_books()
            
            # Show success message
            self.show_message("Success", f"Book '{title}' added successfully!")
            
            # Log for testing/debugging
            print(f"[ADD] Book added: ID={book_id}, Title='{title}'")
            
        except ValueError as e:
            # This catches errors when converting to int or float
            self.show_message("Error", "Invalid input. Check ID and Price is a number")
            print(f"[ERROR] Failed to add book: {e}")

    def clear_entries(self):
        """
        Clear all entry fields after adding a book
        """
        self.id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def show_message(self, title, message):
        """
        Show a popup message window for notifications
        """
        # Create a new window on top of the main window
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x100")
        
        # Add message text
        label = tk.Label(popup, text=message, wraplength=250)
        label.pack(pady=20)
        
        # Add OK button to close the popup
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack()
        
        # Make it modal (must be closed before using main window)
        popup.transient(self.root)
        popup.grab_set()

    def run(self):
        """
        Start the GUI application
        mainloop() keeps the window open and responsive
        """
        self.root.mainloop()


# Test the application if this file is run directly
if __name__ == "__main__":
    # Create my BookstoreGUI object
    app = BookstoreGUI()
    
    # Run the application
    app.run()