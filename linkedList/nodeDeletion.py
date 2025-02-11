from optimizedLL import *
from findLenght import *

def deleteNode(head, pos):
    if pos < 0 or pos >= length(head):
        return head

    if pos == 0:
        return head.next

    count = 0
    prev = None
    curr = head

    while count < pos:
        prev = curr
        curr = curr.next
        count += 1

    if prev is not None:
        prev.next = curr.next

    return head

pos = int(input("Enter the position: "))
head = deleteNode(head,pos)
display(head)
