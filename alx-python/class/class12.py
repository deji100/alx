class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class Singly_linked_list:
    
    def __init__(self):
        self.head = None

    def empty(self):
        if self.head is None:
            return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node 

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next is not None:
            current_node.next = current_node.next.next

    def display(self):
        if self.head is None:
            print("The list is empty.")
        else:
            current_node = self.head
            while current_node.next is not None:
                print("Current Node: {}.".format(current_node.data), end=" -> ")
                current_node = current_node.next

            print("Current Node: {}".format(current_node.data))
            print("Done.")

s = Singly_linked_list()
s.append(1)
s.append(2)
s.append(3)

s.prepend(0)

s.display()

s.delete(0)

s.display()