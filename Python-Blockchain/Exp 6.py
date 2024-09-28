class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the chain

class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node) of the linked list

    def append(self, data):
        """Append a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        """Display the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Example usage:
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()
    # Append blocks to the linked list
    linked_list.append("Block 1")
    linked_list.append("Block 2")
    linked_list.append("Block 3")
    # Display the linked list
    linked_list.display()
