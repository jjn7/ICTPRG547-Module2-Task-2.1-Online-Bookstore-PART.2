# Node class represents one book in linked list
class Node:
    def __init__(self, data):
        self.data = data    # The actual book object stored in node
        self.prev = None    # Pointer to the previous node in the list
        self.next = None    # Pointer to the next node in the list

# DoubleLinkedList
class DoubleLinkedList:
    def __init__(self):
        self.head = None    # Points to the first node in the list
        self.tail = None    # Points to the last node in the list
        self.size = 0       # Track how many books stored
    



    # Add new book to list
    def add_book(self, book):
        # Create a new node and link it
        new_node = Node(book)
        
        if self.head is None: #Check if the list is empty

            # First book in the list - set both head and tail to this node    
            self.head = new_node
            self.tail = new_node

        else:   #List has books - add new book to the end and connect current last book
            self.tail.next = new_node   # Old tail points forward
            new_node.prev = self.tail   # New node points back

            self.tail = new_node    # Update tail to point to our new book (now the last one)

        self.size += 1      # Increase book Count
    



    # Remove book by ID
    def remove_book(self, book_id):
        
        # Check if the list is empty
        if self.head is None:
            print("No books stored")

        # Start from the first book (head) and go through list
        current_node = self.head

        # While loop until end find book with matching ID
        while current_node is not None:
            if current_node.data.id == book_id:     # found book

                # Removes if only the one book in list
                if self.head == self.tail:
                    self.head: None
                    self.tail: None

                # Removes if first book but more there are more after. Changes node head to next book
                elif current_node == self.head:
                    self.head = current_node.next
                    self.head.prev = None

                #Removes if last book but are more befroe. Changes node tail to previous book
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None

                #Removes book fom anywhere in the middle of list. Changes head and tail to previous and next
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev

                #Update book count
                self.size -= 1
                print(f"Removed book: {current_node.data}")
                return True
            
            #move to next book in list
            current_node = current_node.next

            #if book wasn't found
        print(f"Book {book_id} not found")
        return False





    # Show all books in the inventory
    def display_all(self):

    # Check if the list is empty
        if self.head is None:
            print("No books stored")
            return
        
        # Start from the first book (head) and go through list
        current_node = self.head
        book_count = 1
        
        print(f"Displaying ({self.size} books now):")
        print("-" * 50)
        
        # While loop until end of the list
        while current_node is not None:

            # Print current book
            print(f"{book_count}. {current_node.data}")
            
            # Move to the next book
            current_node = current_node.next
            book_count += 1
        
        print("-" * 50)