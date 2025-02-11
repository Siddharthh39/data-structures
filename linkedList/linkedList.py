class Node:
    def __init__(self,data):
        self.data = data # to store the data
        self.next = None # so that the tail is alwas pointing to none

# simple use case
a = Node(13)
b = Node(14) #storing the data at 2 noes self.data will work
a.next = b # to make a refrence

print(a.data)
print(b.data)
print(a.next.data) #by using this u can verify the node class for b

# accessing the memory location
print(a)
print(b) #2 will have have as the refrence for b is stored in node of a
print(a.next)

