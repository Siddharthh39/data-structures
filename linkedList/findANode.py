from optimizedLL import *
from findLenght import *

def findNode(head, n):
    curr = head
    index = 0

    while curr is not None:
        if curr.data == n:
            print(index)
            return
        curr = curr.next
        index += 1

    print (-1)
    return

n = int(input("Enter the Value: "))
findNode(head, n) 
# display(head)
