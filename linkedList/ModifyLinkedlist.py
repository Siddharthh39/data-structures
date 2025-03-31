# def modify(head):
#     left = 0 
#     right = len(head) - 1

#     dummyListOne = []
#     dummyListTwo = []
#     mid = (left + right) // 2

#     while left <= mid:
#             dummyListOne.append(head[left])
#             left += 1

#     while right > mid:
#          dummyListTwo.append(head[right])
#          right -= 1

#     store = []
#     i, j = 0, 0
    
#     lenOfDummyListOne = len(dummyListOne)
#     lenOfDummyListTwo = len(dummyListTwo)

#     while i < lenOfDummyListOne and j < lenOfDummyListTwo:
#          store.append(dummyListOne[i])
#          store.append(dummyListTwo[j])

#          i += 1
#          j += 1

#     while i < lenOfDummyListOne:
#          store.append(dummyListOne[i])
#          i += 1
    
#     while i < lenOfDummyListTwo:
#          store.append(dummyListTwo[j])
#          j += 1

#     return store

# def main():
#     head = [x for x in input("Enter the array: ").split()]
#     print(modify(head))

# if __name__ == "__main__":
#     main()
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_middle(self):
        slow, fast = self.head, self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None  
        return slow 

    def reverse_list(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev  

    def merge_alternate(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            tail.next, l1 = l1, l1.next
            tail = tail.next
            tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2  
        return dummy.next

    def modify(self):
        if not self.head or not self.head.next:
            return
        
        mid = self.find_middle()  
        second_half = self.reverse_list(mid)  
        self.head = self.merge_alternate(self.head, second_half)  



