class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputData = [int(x) for x in input("Enter the data: ").split()]

    head = None
    tail = None

    for currData in inputData:
        if currData == -1:
            break

        newNode = Node(currData)

        if (head) is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode
        
    return head

def display(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
    return

head = takeInput()
display(head)
# # print(head.data)
