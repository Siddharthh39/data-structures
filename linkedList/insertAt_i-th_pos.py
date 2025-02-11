from optimizedLL import *
from findLenght import *

def insertAt_i_Position(head,i,data):
    
    if i<0 or i>length(head):
        return head
    
    count = 0
    prev = None
    curr = head
    
    while count<i:
                
        prev = curr
        curr = curr.next
        count = count+1
    
    newNode = Node(data)
    
    if prev is not None:
        prev.next = newNode
    
    else:
        head = newNode
        
    newNode.next = curr
    
    return head

i = int(input("Enter the index: "))
data = int(input("Enter the input: "))
# print(insertAt_i_Position(head, i, data))

head = insertAt_i_Position(head, i, data)
display(head)