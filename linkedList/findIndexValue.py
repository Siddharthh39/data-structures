from optimizedLL import *

def printIthNode(head, i):
    curr = head
    count = 0
    
    while curr is not None:
        if count == i:
            return curr.data
        
        curr = curr.next
        count += 1

i = int(input("Enter the target index: "))
print(printIthNode(head,i))