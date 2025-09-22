class TreeNode:
    def __init__(self, book):
        self.book = book        # The book stored in this node
        self.left = None        # Left child (books that come "before" this one)
        self.right = None       # Right child (books that come "after" this one)

class BinaryTree:
    def __init__(self):
        self.root = None        # Points to the top node of the tree
        self.size = 0           # Track how many books are in the tree
    
    def add_book(self, book):
        # If tree is empty, make this book the root
        if self.root is None:
            self.root = TreeNode(book)
            self.size += 1
            print(f"Added '{book.title}' as root of tree")
        else:
            # Tree has books - find the right place to insert
            self._insert_recursive(self.root, book)
    
    def _insert_recursive(self, current_node, book):

        # Compare book titles alphabetically
        if book.title.lower() < current_node.book.title.lower():

            # New book comes before current book - go left
            if current_node.left is None:

                # Found empty spot on the left
                current_node.left = TreeNode(book)
                self.size += 1
                print(f"Added '{book.title}' to left of '{current_node.book.title}'")
            else:
                # Keep searching left
                self._insert_recursive(current_node.left, book)
        
        elif book.title.lower() > current_node.book.title.lower():

            # New book comes after current book - go right
            if current_node.right is None:

                # Found empty spot on the right
                current_node.right = TreeNode(book)
                self.size += 1
                print(f"Added '{book.title}' to right of '{current_node.book.title}'")
            else:
                # Keep searching right
                self._insert_recursive(current_node.right, book)
        else:
            # Book titles are the same - don't add duplicates
            print(f"Book '{book.title}' already exists in tree")
    


    def search_by_title(self, title):
        # Start searching from the root
        return self._search_recursive(self.root, title)
    


    def _search_recursive(self, current_node, title):
        # Base case: reached end of tree or found empty spot
        if current_node is None:
            return None
        

    
        # Compare titles
        if title.lower() == current_node.book.title.lower():
            # Found the book!
            return current_node.book
        elif title.lower() < current_node.book.title.lower():
            # Search left side
            return self._search_recursive(current_node.left, title)
        else:
            # Search right side
            return self._search_recursive(current_node.right, title)
    


    def display_all_sorted(self):
        # Display books in alphabetical order
        print(f"Books in alphabetical order ({self.size} total):")
        print("-" * 50)
        self._inorder_traversal(self.root)
        print("-" * 50)
    


    def _inorder_traversal(self, current_node):
        # In-order: left -> current -> right (gives alphabetical order)
        if current_node is not None:

            # First, visit all books on the left (earlier alphabetically)
            self._inorder_traversal(current_node.left)

            # Then, print the current book
            print(f"  {current_node.book}")
            
            # Finally, visit all books on the right (later alphabetically)
            self._inorder_traversal(current_node.right)