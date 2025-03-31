class LinearQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value = self.queue[self.front]
            self.front += 1
            if self.front > self.rear:
                self.front = self.rear = -1
            return value

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.queue[self.front]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.size - 1
