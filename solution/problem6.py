class Node:
    def __init__(self, value):
        self.value = value
        self.both = 0  # Will store XOR of prev and next node addresses

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = {}  # Simulated memory storage for address lookups

    def get_pointer(self, node):
        """Simulates getting a memory address for a node."""
        if node is None:
            return 0  # Null reference
        return id(node)

    def dereference_pointer(self, address):
        """Simulates getting a node from a memory address."""
        return self.nodes.get(address, None)

    def add(self, element):
        """Adds a new element to the end of the XOR linked list."""
        new_node = Node(element)
        self.nodes[self.get_pointer(new_node)] = new_node  # Store in simulated memory

        if self.head is None:  # First node
            self.head = self.tail = new_node
        else:
            # Update the new node's both to be XOR of previous node and None (0)
            new_node.both = self.get_pointer(self.tail) ^ 0

            # Update the previous tail's both field
            self.tail.both ^= self.get_pointer(new_node)

            # Move the tail pointer to the new node
            self.tail = new_node

    def get(self, index):
        """Retrieves the node at the given index."""
        prev_addr = 0
        current = self.head

        for i in range(index):
            if current is None:
                raise IndexError("Index out of bounds")

            next_addr = prev_addr ^ current.both  # Compute next node address
            prev_addr = self.get_pointer(current)  # Update prev to current
            current = self.dereference_pointer(next_addr)  # Move to the next node

        if current is None:
            raise IndexError("Index out of bounds")
        return current.value
    

if __name__ == '__main__':
    xor_list = XORLinkedList()
    xor_list.add(1)
    xor_list.add(2)
    xor_list.add(3)
    xor_list.add(4)

    print(xor_list.get(0))  # Output: 1
    print(xor_list.get(1))  # Output: 2
    print(xor_list.get(2))  # Output: 3
    print(xor_list.get(3))  # Output: 4