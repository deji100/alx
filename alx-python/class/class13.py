class Node:
    """A Node class that creates new node instances"""

    def __init__(self, data, next_node=None):
        """
        A method that initializes a new node instance

        arguments:
            data: provided by the user

            next_node: a private att to point to the next node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """A method that gets data for a node instance"""

        return self.__data

    @data.setter
    def data(self, value):
        """A method that sets data for a node instance"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """A method that gets the next node instance"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """A method that sets the next node instance"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A singlyLinkedList class"""

    def __init__(self):
        """Initializes the private head instance att to None"""

        self.__head = None

    def sorted_insert(self, value):
        """Sort the Node according to node instance data"""

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while current_node.next_node is not None and current_node.next_node.data < new_node.data:
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """Returns a string of linked_list data with new line"""

        linked_lists = []
        current_node = self.__head
        while current_node is not None:
            linked_lists.append(str(current_node.data))
            current_node = current_node.next_node

        return "\n".join(linked_lists)
    
s = SinglyLinkedList()

s.sorted_insert(4)
s.sorted_insert(6)
s.sorted_insert(9)
s.sorted_insert(2)
s.sorted_insert(3)

print(s)