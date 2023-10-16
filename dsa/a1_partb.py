#    Main Author(s): Lovejeet Singh
#    Main Reviewer(s): Tanisha Sharma


# Define a Node class for the elements in the Doubly Linked List
class Node:
    def __init__(self, data=None, next_node=None, previous_node=None):
        # Initialize the node with data, a reference to the next node, and a reference to the previous node
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_previous(self):
        return self.previous_node

# Define a DoublyLinked class for the Doubly Linked List itself
class DoublyLinked:
    def __init__(self):
        # Initialize an empty Doubly Linked List with front, back, and size attributes
        self.front = None
        self.back = None
        self.size = 0

    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    def push_front(self, data):
        # Add data to the front of the list
        new_node = Node(data)
        if self.is_empty():
            # If the list is empty, the new node becomes both front and back
            self.front = self.back = new_node
        else:
            # Otherwise, update references to add the new node to the front
            new_node.next_node = self.front
            self.front.previous_node = new_node
            self.front = new_node
        self.size += 1

    def push_back(self, data):
        # Add data to the back of the list
        new_node = Node(data)
        if self.is_empty():
            # If the list is empty, the new node becomes both front and back
            self.front = self.back = new_node
        else:
            # Otherwise, update references to add the new node to the back
            new_node.previous_node = self.back
            self.back.next_node = new_node
            self.back = new_node
        self.size += 1

    def pop_front(self):
        # Remove and return the front element
        if self.is_empty():
            raise IndexError('pop_front() used on empty list')
        data = self.front.data
        if self.size == 1:
            self.front = self.back = None
        else:
            self.front = self.front.next_node
            self.front.previous_node = None
        self.size -= 1
        return data

    def pop_back(self):
        # Remove and return the back element
        if self.is_empty():
            raise IndexError('pop_back() used on empty list')
        data = self.back.data
        if self.size == 1:
            self.front = self.back = None
        else:
            self.back = self.back.previous_node
            self.back.next_node = None
        self.size -= 1
        return data

    def is_empty(self):
        # Check if the list is empty
        return self.size == 0

    def insert_after(self, data, node):
        # Insert data after a given node (or at the front if node is None)
        if node is None:
            self.push_front(data)
        else:
            new_node = Node(data)
            new_node.next_node = node.next_node
            new_node.previous_node = node
            if node.next_node is not None:
                node.next_node.previous_node = new_node
            node.next_node = new_node
            self.size += 1

    def search(self, data):
        # Search for a node with a specific data value
        current_node = self.front
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_node
        return None

    def __len__(self):
        # Get the size of the list
        return self.size

    def is_palindrome(self):
        def is_palindrome_recursive(front, back):
            # Recursive helper function to check if the list is a palindrome
            if front is None or back is None:
                return True
            if front.data != back.data:
                return False
            return is_palindrome_recursive(front.next_node, back.previous_node)

        return is_palindrome_recursive(self.front, self.back)

# Example usage:
if __name__ == "__main__":
    linked_list = DoublyLinked()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    linked_list.push_back(2)
    linked_list.push_back(1)

    # Check if the linked list is a palindrome
    print(linked_list.is_palindrome())  # True

    linked_list.pop_back()
    linked_list.push_back(5)

    # Check if the linked list is still a palindrome
    print(linked_list.is_palindrome())  # False