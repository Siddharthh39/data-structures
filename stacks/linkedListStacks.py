class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        while self.isEmpty() is True:
            print("Stack is empty")
            return

        data = self.__head
        self.__head = self.__head.next
        self.__count -= 1
        return data.data

    def size(self):
        return self.__count

    def top(self):
        while self.isEmpty() is True:
            print("Stack is empty")
            return
        
        data = self.__head
        return data.data

    def isEmpty(self):
        return self.size() == 0
    
    def checkStack(self):
        curr = self.__head 
        
        if self.isEmpty() is True:
            print("Stack is empty")

        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("-1")
        