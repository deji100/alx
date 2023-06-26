class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

print(n1.data)
print(n1.next.data)
print(n1.next.next.data)
print(n1.next.next.next == None)
print(n3.next == None)