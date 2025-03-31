class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinearQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return value

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.front.value

    def isEmpty(self):
        return self.front is None
