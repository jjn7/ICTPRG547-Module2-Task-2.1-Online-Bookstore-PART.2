# Import custom classes from other files
from models.book import Book
from data_structures.linked_list import DoubleLinkedList
from data_structures.hash_table import HashTable
from data_structures.binary_tree import BinaryTree

# Main function 
def main():
    # Initialize data structures
    inventory = DoubleLinkedList()
    quick_lookup = HashTable()  # Including Hash Table
    tree_lookup = BinaryTree()  # Including Binary Tree
    
    # Test with sample books
    book1 = Book(12345, "Harry Potter", "J.K. Rowling", "Fantasy", 29.99)
    book2 = Book(67890, "Animal Farm", "George Orwell", "Fiction", 19.99)
    book3 = Book(23456, "The Great Gatsby", "F. Scott Fitzgerald", "Historical Fiction", 24.99)
    
    # Print header
    print("Bookstore Inventory")
    print("=" * 30)
    
    # TESTING BINARY TREE OUTPUT
    print("\n" + "=" * 30)
    print("Testing Binary Tree:")
    print("=" * 30)

    tree_lookup.add_book(book1) # Harry Potter Becomes Root
    tree_lookup.add_book(book2) # Animal Farm added to left of HP (Alphabetical order)
    tree_lookup.add_book(book3) # The Great Gatsby goes right of HP (Alphabetical order)
    
    # Display hash table contents
    tree_lookup.display_all_sorted()

    # Test finding existing book
    print("\nTesting book lookups:")
    found_book = tree_lookup.search_by_title("Harry Potter")
    if found_book:
        print(f"Found: {found_book}")
    else:
        print("Book not found")
    
    # Test finding non-existent book
    not_found = tree_lookup.search_by_title("LOTR")
    if not_found:
        print(f"Found: {not_found}")
    else:
        print("Book not found (as expected)")

# only run main() if this file is run directly (not if it's imported by another file)
# Every Python file has a built-in variable called __name__. Python automatically sets this variable differently depending on how the file is used.
if __name__ == "__main__":
    main()