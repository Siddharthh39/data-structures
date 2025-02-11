from optimizedLL import *
from findLenght import *

def appendLastNToFirst(head, n):
    
    curr = head
    count = length(head)

    while curr is not None:
        
        print(curr.data)
        curr = curr.next

    return 

n = int(input("enter the value: "))
head = appendLastNToFirst(head,n)
print(head)

