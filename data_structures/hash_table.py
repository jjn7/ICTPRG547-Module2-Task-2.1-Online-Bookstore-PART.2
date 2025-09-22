class HashTable:
    def __init__(self, size=10):
        # size=10 is just a starting point for testing
        # The size affects performance - bigger = fewer collisions but more memory
        self.size = size
        
        # Create an array of empty lists
        # Each position will hold a list of books (handles collisions) # [[], [], [], .... 10 empty lists
        self.table = [[] for _ in range(size)]
        
        # Keep track of total books stored
        self.count = 0
    
    def _hash_function(self, book_id):
        # underscore means this is a "private" method (internal use)
        
        # Hash function: converts book ID to array position
        # book_id 12345 → 12345 % 10 = 5 (to position 5)
        # book_id 67890 → 67890 % 10 = 0 (to position 0)
        return book_id % self.size
    
    def add_book(self, book):
        # Determine which array position this book belongs
        index = self._hash_function(book.id)
        
        # Check if this book ID already exists at this position
        for existing_book in self.table[index]:
            if existing_book.id == book.id:
                print(f"Book ID {book.id} already exists in hash table")
                return False
        
        # Add the book to the list
        # If position 5 empty: [] becomes [book]
        # If position 5 contains book: [book1] becomes [book1, book2]
        self.table[index].append(book)
        self.count += 1
        print(f"Added book ID {book.id} to hash position {index}")
        return True
    

    def find_book(self, book_id):
        # Calculate where the book should be
        index = self._hash_function(book_id)
        
        # Search through books at this position
        for book in self.table[index]:
            if book.id == book_id:
                return book
        
        # Book not found
        return None
    
    def remove_book(self, book_id):
        # Calculate position
        index = self._hash_function(book_id)
        
        # Search and remove
        for i, book in enumerate(self.table[index]):
            if book.id == book_id:
                removed_book = self.table[index].pop(i)
                self.count -= 1
                print(f"Removed book: {removed_book}")
                return True
        
        print(f"Book ID {book_id} not found in hash table")
        return False
    
    def display_all(self):
        print(f"Hash Table Contents ({self.count} books):")

        #search through each table position
        for i, book_list in enumerate(self.table):
            if book_list:  # Only show positions that have books
                print(f"Position {i}:")
                # Print each book at this position
                for book in book_list:
                    print(f"  - {book}")
        
        print("-" * 40)