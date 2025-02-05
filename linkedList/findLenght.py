from optimizedLL import *

# def length(head):
#     count = 0
#     currPos = head

#     while currPos is not None:
#         count += 1
#         currPos = currPos.next
    
#     return count
def length(head):
    if head is None:
        return 0
    
    count = 0

    while head:
        count += 1
        head = head.next

    return count

# print(length(head))
