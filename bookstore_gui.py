# Basic GUI Window for Bookstore Application

# Import tkinter - Python's built-in GUI library
import tkinter as tk
from tkinter import filedialog  # For file browser dialog

# Import my classes from Part 1
from models.book import Book
from data_structures.linked_list import DoubleLinkedList
from data_structures.hash_table import HashTable
from data_structures.binary_tree import BinaryTree

# Import my image validation utility (uses Pillow library)
from utils.image_validator import validate_image

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
        self.root.geometry("900x750")

        # Set background color
        self.root.config(bg="#f5f5f5")

        # Define color scheme
        self.bg_color = "#f5f5f5"
        self.frame_bg = "#ffffff"
        self.button_bg = "#4a4a4a"
        self.button_fg = "#ffffff"
        self.accent_color = "#2c5f7d"

        # Initialize data structures from Part 1
        # These are the same structures I used in main.py
        self.inventory = DoubleLinkedList()  # For storing books in order
        self.quick_lookup = HashTable()      # For fast ID-based searches
        self.tree_lookup = BinaryTree()      # For alphabetical sorting/searching

        # Add some sample books
        self.load_sample_books()

        # Header section
        header_frame = tk.Frame(self.root, bg=self.accent_color)
        header_frame.pack(fill="x", pady=(0, 15))

        welcome_label = tk.Label(header_frame, text="Bookstore Inventory System",
                                font=("Arial", 16, "bold"), bg=self.accent_color, fg="white")
        welcome_label.pack(pady=12)

        # Book count label
        self.book_count_label = tk.Label(self.root, text=f"Books loaded: {self.inventory.size}",
                                        font=("Arial", 10), bg=self.bg_color)
        self.book_count_label.pack(pady=(0, 8))

        # View button
        view_button = tk.Button(self.root, text="View Books", command=self.view_books,
                               font=("Arial", 10), bg=self.button_bg, fg=self.button_fg,
                               padx=20, pady=6, relief="flat", cursor="hand2")
        view_button.pack(pady=(0, 10))

        # Text area with frame
        text_frame = tk.Frame(self.root, bg=self.bg_color)
        text_frame.pack(padx=20, pady=(0, 10), fill="both", expand=True)

        self.text_area = tk.Text(text_frame, height=15, width=80,
                                font=("Courier New", 9), relief="solid",
                                borderwidth=1, padx=10, pady=10)
        self.text_area.pack(fill="both", expand=True)

        # Show initial instructions
        self.show_instructions()

        # Add the new Add/Edit Book frame after creating the text area
        self.create_add_book_frame()

    def load_sample_books(self):
        """
        Loads some sample books into the data structures
        This provides data to work with for testing the GUI
        """

        # Create sample books
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
        
        # Update book count label
        self.book_count_label.config(text=f"Books loaded: {self.inventory.size}")

    def create_add_book_frame(self):
        """
        Create a frame with input fields for adding and editing books
        Grid layout used
        """

        # LabelFrame creates a bordered box with a title
        add_frame = tk.LabelFrame(self.root, text="Add/Edit/Delete Book",
                                 font=("Arial", 11, "bold"), padx=15, pady=15,
                                 bg=self.frame_bg, relief="solid", borderwidth=1)

        # pack() places the frame on the window
        # fill="x" makes it stretch horizontally
        add_frame.pack(padx=20, pady=(0, 20), fill="x")
        
        # Using grid layout to arrange input fields in rows and columns
        # Configure column weights for proper stretching
        add_frame.columnconfigure(1, weight=1)
        add_frame.columnconfigure(3, weight=1)

        # ROW 0: Book ID and Title
        tk.Label(add_frame, text="Book ID: *", font=("Arial", 9), bg=self.frame_bg).grid(row=0, column=0, sticky="w", pady=6)

        # References to Entry widgets to get their values later
        self.id_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.id_entry.grid(row=0, column=1, padx=5, pady=6, sticky="ew")

        tk.Label(add_frame, text="Title: *", font=("Arial", 9), bg=self.frame_bg).grid(row=0, column=2, sticky="w", padx=(15, 0), pady=6)
        self.title_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.title_entry.grid(row=0, column=3, padx=5, pady=6, sticky="ew")

        # ROW 1: Author and Genre
        tk.Label(add_frame, text="Author: *", font=("Arial", 9), bg=self.frame_bg).grid(row=1, column=0, sticky="w", pady=6)
        self.author_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.author_entry.grid(row=1, column=1, padx=5, pady=6, sticky="ew")

        tk.Label(add_frame, text="Genre: *", font=("Arial", 9), bg=self.frame_bg).grid(row=1, column=2, sticky="w", padx=(15, 0), pady=6)
        self.genre_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.genre_entry.grid(row=1, column=3, padx=5, pady=6, sticky="ew")

        # ROW 2: Price and Cover Image
        tk.Label(add_frame, text="Price: *", font=("Arial", 9), bg=self.frame_bg).grid(row=2, column=0, sticky="w", pady=6)
        self.price_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.price_entry.grid(row=2, column=1, padx=5, pady=6, sticky="ew")

        tk.Label(add_frame, text="Cover Image:", font=("Arial", 9), bg=self.frame_bg).grid(row=2, column=2, sticky="w", padx=(15, 0), pady=6)

        # Frame to hold image path entry and browse button together
        image_frame = tk.Frame(add_frame, bg=self.frame_bg)
        image_frame.grid(row=2, column=3, sticky="ew", pady=6, padx=5)

        self.image_entry = tk.Entry(image_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.image_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        # Browse button to open file dialog
        browse_button = tk.Button(image_frame, text="Browse...", command=self.browse_image,
                                 font=("Arial", 8), bg="#e0e0e0", fg="black",
                                 relief="flat", cursor="hand2", padx=8, pady=2)
        browse_button.pack(side="left")

        # ROW 3: Action Buttons
        add_button = tk.Button(add_frame, text="Add Book", command=self.add_book,
                              font=("Arial", 9), bg=self.button_bg, fg=self.button_fg,
                              relief="flat", cursor="hand2", padx=12, pady=6)
        add_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        edit_button = tk.Button(add_frame, text="Edit Book", command=self.edit_book,
                               font=("Arial", 9), bg=self.button_bg, fg=self.button_fg,
                               relief="flat", cursor="hand2", padx=12, pady=6)
        edit_button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

        # ROW 4: Select and Load for editing
        tk.Label(add_frame, text="Select Book ID to Edit:", font=("Arial", 9), bg=self.frame_bg).grid(row=4, column=0, sticky="w", pady=6)
        self.select_id_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.select_id_entry.grid(row=4, column=1, padx=5, pady=6, sticky="ew")

        # Load button to populate fields with selected book's data
        load_button = tk.Button(add_frame, text="Load Book", command=self.load_book_for_edit,
                               font=("Arial", 9), bg=self.button_bg, fg=self.button_fg,
                               relief="flat", cursor="hand2", padx=12, pady=6)
        load_button.grid(row=4, column=2, padx=5, pady=6, sticky="ew")

        # ROW 5: Delete Book Section
        tk.Label(add_frame, text="Delete Book by ID:", font=("Arial", 9), bg=self.frame_bg).grid(row=5, column=0, sticky="w", pady=6)
        self.delete_id_entry = tk.Entry(add_frame, font=("Arial", 9), relief="solid", borderwidth=1)
        self.delete_id_entry.grid(row=5, column=1, padx=5, pady=6, sticky="ew")

        # Delete button
        delete_button = tk.Button(add_frame, text="Delete Book", command=self.confirm_delete,
                                font=("Arial", 9), bg="#8b4545", fg="white",
                                relief="flat", cursor="hand2", padx=12, pady=6)
        delete_button.grid(row=5, column=2, padx=5, pady=6, sticky="ew")

        # Clear All button
        clear_all_button = tk.Button(add_frame, text="Clear All Fields", command=self.clear_all_fields,
                                    font=("Arial", 9), bg="#6b6b6b", fg="white",
                                    relief="flat", cursor="hand2", padx=12, pady=6)
        clear_all_button.grid(row=5, column=3, padx=5, pady=6, sticky="ew")

        # Add required field note
        tk.Label(add_frame, text="* Required field", font=("Arial", 8, "italic"),
                bg=self.frame_bg, fg="#666666").grid(row=6, column=0, columnspan=4, sticky="w", pady=(5, 0))

    def show_instructions(self):
        """
        Display initial instructions in the text area
        """
        instructions = """Welcome to the Bookstore Inventory System

Getting Started:

  1. View Books - Click the 'View Books' button to see all books in inventory

  2. Add a Book - Fill in the required fields (*) and click 'Add Book'

  3. Edit a Book - Enter a Book ID in 'Select Book ID to Edit', click 'Load Book',
     make your changes, then click 'Edit Book'

  4. Delete a Book - Enter a Book ID in 'Delete Book by ID' and click 'Delete Book'

Note: Fields marked with * are required
"""
        self.text_area.insert(tk.END, instructions)

    def add_book(self):
        """
        Add a new book to all data structures
        """

        # Using try/except to handle potential errors (like invalid numbers)
        try:
            # Get values from my input fields
            book_id = int(self.id_entry.get())
            title = self.title_entry.get().strip()
            author = self.author_entry.get().strip()
            genre = self.genre_entry.get().strip()
            price = float(self.price_entry.get())
            image_path = self.image_entry.get().strip()

            # Validate that all fields are filled
            if not title or not author or not genre:
                self.show_message("Error", "Please fill in all fields")
                return

            # Check price is valid
            if price < 0:
                self.show_message("Error", "Price cannot be negative")
                return

            # Validate cover image if provided (using Pillow library)
            if image_path:
                is_valid, message = validate_image(image_path)
                if not is_valid:
                    self.show_message("Error", f"Image validation failed: {message}")
                    print(f"[ERROR] Image validation: {message}")
                    return
                else:
                    print(f"[INFO] Image validated: {message}")

            # Check if book ID already exists using my hash table
            if self.quick_lookup.find_book(book_id):
                self.show_message("Error", f"Book with ID {book_id} already exists")
                return

            # Create new book object with optional image path
            new_book = Book(book_id, title, author, genre, price, image_path=image_path if image_path else None)

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
            if image_path:
                print(f"[ADD] Cover image: {image_path}")

        except ValueError as e:
            # This catches errors when converting to int or float
            self.show_message("Error", "Invalid input. Check ID and Price is a number")
            print(f"[ERROR] Failed to add book: {e}")

    def load_book_for_edit(self):
        """
        Load an existing book's details into the input fields for editing
        Using the hash table for quick lookup by ID
        """
        try:
            # Get the ID from the selection field
            book_id = int(self.select_id_entry.get())
            
            # Use hash table to find the book quickly
            book = self.quick_lookup.find_book(book_id)
            
            if book is None:
                # Book not found
                self.show_message("Error", f"No book found with ID {book_id}")
                return
            
            # Clear all fields first
            self.clear_entries()

            # Populate fields with the book's current data
            # This allows the user to see current values and change what they need
            self.id_entry.insert(0, str(book.book_id))
            self.title_entry.insert(0, book.title)
            self.author_entry.insert(0, book.author)
            self.genre_entry.insert(0, book.genre)
            self.price_entry.insert(0, str(book.price))

            # Load image path if it exists
            if book.image_path:
                self.image_entry.insert(0, book.image_path)
            
            # Disable the ID field since we shouldn't change IDs
            # This prevents creating duplicate IDs
            self.id_entry.config(state='readonly')
            
            # Show confirmation that book was loaded
            self.show_message("Success", f"Book '{book.title}' loaded for editing")
            
            # Log for testing
            print(f"[LOAD] Book loaded for editing: ID={book_id}, Title='{book.title}'")
            
        except ValueError:
            self.show_message("Error", "Please enter a valid book ID number")
            print(f"[ERROR] Invalid ID entered for loading")

    def edit_book(self):
        """
        Edit an existing book's details
        This updates the book in all three data structures
        """
        try:
            # Check if ID field is readonly (means we're editing)
            if str(self.id_entry.cget('state')) != 'readonly':
                self.show_message("Error", "Please load a book first using the Load Book button")
                return

            # Get the values from input fields
            book_id = int(self.id_entry.get())
            new_title = self.title_entry.get().strip()
            new_author = self.author_entry.get().strip()
            new_genre = self.genre_entry.get().strip()
            new_price = float(self.price_entry.get())
            new_image_path = self.image_entry.get().strip()

            # Validate inputs
            if not new_title or not new_author or not new_genre:
                self.show_message("Error", "Please fill in all fields")
                return

            if new_price < 0:
                self.show_message("Error", "Price cannot be negative")
                return

            # Validate cover image if provided (using Pillow library)
            if new_image_path:
                is_valid, message = validate_image(new_image_path)
                if not is_valid:
                    self.show_message("Error", f"Image validation failed: {message}")
                    print(f"[ERROR] Image validation: {message}")
                    return
                else:
                    print(f"[INFO] Image validated: {message}")

            # Find the existing book in hash table
            old_book = self.quick_lookup.find_book(book_id)

            if old_book is None:
                self.show_message("Error", "Book no longer exists in inventory")
                return

            # Store old title for binary tree update (since tree is sorted by title)
            old_title = old_book.title

            # Update the book object with new values
            # updating the object updates it everywhere
            old_book.title = new_title
            old_book.author = new_author
            old_book.genre = new_genre
            old_book.price = new_price
            old_book.image_path = new_image_path if new_image_path else None

            # Special handling for binary tree if title changed
            # Tree needs reorganising if the sort key (title) changed
            if old_title != new_title:
                # Remove old entry and add with new title
                # maintains proper alphabetical ordering
                self.tree_lookup.root = self._remove_from_tree(self.tree_lookup.root, old_title)
                self.tree_lookup.add_book(old_book)
                print(f"[EDIT] Book title changed, reorganized in binary tree")

            # Clear the selection and input fields
            self.clear_entries()
            self.select_id_entry.delete(0, tk.END)

            # Re-enable the ID field for next operation
            self.id_entry.config(state='normal')

            # Refresh the display
            self.view_books()

            # Show success message
            self.show_message("Success", f"Book '{new_title}' updated successfully!")

            # Log for testing
            print(f"[EDIT] Book updated: ID={book_id}, New Title='{new_title}'")
            if new_image_path:
                print(f"[EDIT] Cover image: {new_image_path}")

        except ValueError as e:
            self.show_message("Error", "Invalid input. Please check ID and Price are numbers")
            print(f"[ERROR] Failed to edit book: {e}")

    def _remove_from_tree(self, node, title):
        """
        remove a node from binary tree by title
        """
        if node is None:
            return node
        
        # Navigate to find the node to remove
        if title < node.data.title:
            node.left = self._remove_from_tree(node.left, title)
        elif title > node.data.title:
            node.right = self._remove_from_tree(node.right, title)
        else:
            # Found the node to remove
            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Two children
            # Find the minimum node in right subtree
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._remove_from_tree(node.right, min_node.data.title)
        
        return node

    def _find_min(self, node):
        """
        Find the leftmost (minimum) node in a tree
        Used by the remove function
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def browse_image(self):
        """
        Open a file browser dialog to select an image file
        Automatically populates the image_entry field with the selected path
        """
        # Open file dialog - only show image files
        file_path = filedialog.askopenfilename(
            title="Select Book Cover Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )

        # If user selected a file (didn't cancel)
        if file_path:
            # Clear current entry and insert the selected path
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, file_path)
            print(f"[BROWSE] Image selected: {file_path}")

    def clear_entries(self):
        """
        Clear all entry fields and reset ID field state
        """
        # Make sure ID field is editable before clearing
        self.id_entry.config(state='normal')

        self.id_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.image_entry.delete(0, tk.END)

    def show_message(self, title, message):
        """
        Show a popup message window for notifications
        """
        # Create a new window on top of the main window
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("350x120")
        popup.config(bg=self.frame_bg)

        # Add message text
        label = tk.Label(popup, text=message, wraplength=300,
                        font=("Arial", 9), bg=self.frame_bg)
        label.pack(pady=20)

        # Add OK button to close the popup
        ok_button = tk.Button(popup, text="OK", command=popup.destroy,
                             font=("Arial", 9), bg=self.button_bg, fg=self.button_fg,
                             relief="flat", cursor="hand2", padx=20, pady=6)
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




    def confirm_delete(self):
        """
        confirmation dialog before deleting a book
        """
        try:
            # Get the book ID to delete
            book_id = int(self.delete_id_entry.get())

            # check if the book exists using hash table
            book = self.quick_lookup.find_book(book_id)

            if book is None:
                self.show_message("Error", f"No book found with ID {book_id}")
                return

            # Create confirmation dialog
            confirmation_popup = tk.Toplevel(self.root)
            confirmation_popup.title("Confirm Deletion")
            confirmation_popup.geometry("420x170")
            confirmation_popup.config(bg=self.frame_bg)

            # Warning message with book details
            warning_text = f"Are you sure you want to delete this book?\n\n"
            warning_text += f"ID: {book.book_id}\n"
            warning_text += f"Title: {book.title}\n"
            warning_text += f"Author: {book.author}\n\n"
            warning_text += "This action cannot be undone!"

            label = tk.Label(confirmation_popup, text=warning_text, justify="left",
                           font=("Arial", 9), bg=self.frame_bg)
            label.pack(pady=15)

            # Button frame for Yes/No buttons
            button_frame = tk.Frame(confirmation_popup, bg=self.frame_bg)
            button_frame.pack(pady=10)

            # Yes button
            yes_button = tk.Button(button_frame, text="Yes, Delete",
                                command=lambda: self.delete_book(book_id, confirmation_popup),
                                font=("Arial", 9), bg="#8b4545", fg="white",
                                relief="flat", cursor="hand2", padx=15, pady=6, width=12)
            yes_button.pack(side="left", padx=5)

            # No button - cancel deletion
            no_button = tk.Button(button_frame, text="Cancel",
                                command=confirmation_popup.destroy,
                                font=("Arial", 9), bg=self.button_bg, fg="white",
                                relief="flat", cursor="hand2", padx=15, pady=6, width=12)
            no_button.pack(side="left", padx=5)

            # Make it modal
            confirmation_popup.transient(self.root)
            confirmation_popup.grab_set()

        except ValueError:
            self.show_message("Error", "Please enter a valid book ID number")
            print(f"[ERROR] Invalid ID")


    def delete_book(self, book_id, popup_window):
        """
        Actually delete the book from all data structures after confirmation
        """
        try:
            # Get book details before deletion for logging
            book = self.quick_lookup.find_book(book_id)
            
            if book is None:
                self.show_message("Error", "Book no longer exists")
                popup_window.destroy()
                return
        
            # Store book details for success message
            book_title = book.title
            
            # Remove from hash table
            delete_success = self.quick_lookup.remove_book(book_id)
            
            if not delete_success:
                self.show_message("Error", "Failed to delete from hash table")
                popup_window.destroy()
                return
        
            # Remove from linked list
            self.delete_from_linked_list(book_id)
            
            # Remove from binary tree (by title)
            self.tree_lookup.root = self._remove_from_tree(self.tree_lookup.root, book_title)
            
            # Close confirmation popup
            popup_window.destroy()
            
            # Clear the delete ID field
            self.delete_id_entry.delete(0, tk.END)
            
            # Refresh the display
            self.view_books()
            
            # Show success message
            self.show_message("Success", f"Book '{book_title}' has been deleted from inventory")
            
            # Log for testing
            print(f"[DELETE] Book deleted: ID={book_id}, Title='{book_title}'")
            print(f"[DELETE] Remaining books in inventory: {self.inventory.size}")
            
        except Exception as e:
            self.show_message("Error", f"Failed to delete book: {str(e)}")
            popup_window.destroy()
            print(f"[ERROR] Exception during deletion: {e}")


    def delete_from_linked_list(self, book_id):
        """
        Remove a book from the double linked list by ID
        Handles all the pointer adjustments for double linking
        """
        current = self.inventory.head
        
        while current is not None:
            if current.data.book_id == book_id:
                # Found the node to delete
                
                # If deleting the head node
                if current == self.inventory.head:
                    self.inventory.head = current.next
                    if self.inventory.head:
                        self.inventory.head.prev = None
                    else:
                        # List is now empty
                        self.inventory.tail = None
                
                # If deleting the tail node
                elif current == self.inventory.tail:
                    self.inventory.tail = current.prev
                    if self.inventory.tail:
                        self.inventory.tail.next = None
                
                # If deleting a middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                # Decrease the size
                self.inventory.size -= 1
                
                print(f"[DELETE] Book removed from linked list. New size: {self.inventory.size}")
                return True
            
            current = current.next
        
        print(f"[WARNING] Book ID {book_id} not found in linked list")
        return False

  
    def clear_all_fields(self):
        """
        Clear all input fields including the delete and select fields
        Useful for resetting the form completely
        """
        # Clear main input fields
        self.clear_entries()
        
        # Clear selection field
        if hasattr(self, 'select_id_entry'):
            self.select_id_entry.delete(0, tk.END)
        
        # Clear delete field
        if hasattr(self, 'delete_id_entry'):
            self.delete_id_entry.delete(0, tk.END)
        
        # Make sure ID field is editable
        self.id_entry.config(state='normal')
        
        print("[CLEAR] All fields cleared")

    

# Test the application if this file is run directly
if __name__ == "__main__":
    # Create my BookstoreGUI object
    app = BookstoreGUI()
    
    # Run the application
    app.run()