from optimizedLL import*

def reverseLinkedList(head):
    if head is None:
        return None
    
    if head.next is None:
        return head
    
    smallHead = reverseLinkedList(head.next)
    curr = smallHead

    while curr.next is not None:
        curr = curr.next

    curr.next = head
    head.next = None

    return smallHead
        


rh = reverseLinkedList(head)
display(rh)