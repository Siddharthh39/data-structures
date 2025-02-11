class Node:
    # Constructor to create a node with data and a reference to the next node
    def __init__(self, data):
        self.data = data  # Stores the data value
        self.next = None  # Pointer to the next node (initially None)

def takingInput():
    # Take input from the user and convert it into a list of integers
    inputList = [int(x) for x in input("Enter the input: ").split()]

    head = None  # Initialize the head of the linked list as None

    for currData in inputList:
        if currData == -1:  # Stop reading input when -1 is encountered
            break

        newNode = Node(currData)  # Create a new node with the current data

        if head is None:  # If the list is empty, set the head to the new node
            head = newNode
        else:
            # Traverse to the end of the list to append the new node
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode  # Link the last node to the new node

    return head  # Return the head of the linked list

def display(head):
    # Traverse the list and display each node's data
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")  # End of the linked list
    return

# Create the linked list from user input
head = takingInput()

# Display the linked list
display(head)

# Print the data of the head node
print(head.data)
