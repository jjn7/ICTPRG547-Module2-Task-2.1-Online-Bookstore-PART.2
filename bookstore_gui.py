# Basic GUI Window for Bookstore Application
# Step 2: Adding data structure integration

# Import tkinter - Python's built-in GUI library
import tkinter as tk

# Import classes from Part 1
from models.book import Book
from data_structures.linked_list import DoubleLinkedList
from data_structures.hash_table import HashTable
from data_structures.binary_tree import BinaryTree

class BookstoreGUI:
    """
    Main class for the bookstore GUI application
    Starting with just a basic window that can open and close
    """

    def __init__(self):
        """
        Constructor - sets up the basic window and data structures
        This runs when we create a new BookstoreGUI object
        """

        # Create the main window using tkinter
        self.root = tk.Tk()

        # Set the window title (appears in title bar)
        self.root.title("Online Bookstore Inventory System")

        # Set the window size (width x height in pixels)
        self.root.geometry("800x600")

        # Initialize data structures from Part 1
        # These are the same structures used in main.py
        self.inventory = DoubleLinkedList()  # For storing books in order
        self.quick_lookup = HashTable()      # For fast ID-based searches
        self.tree_lookup = BinaryTree()      # For alphabetical sorting/searching

        # Add some sample books so we have data to work with
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

    def run(self):
        """
        Start the GUI application
        This keeps the window open and responsive to user interactions
        mainloop() is what makes the window stay on screen
        """
        self.root.mainloop()

# Test the basic window if this file is run directly
if __name__ == "__main__":
    # Create a new BookstoreGUI object
    app = BookstoreGUI()

    # Run the application (this opens the window)
    app.run()