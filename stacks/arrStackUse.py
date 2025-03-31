# from arrayStacks import *
from linkedListStacks import *
s = Stack()
s.push(12)
s.push(14)
s.push(13)
# print(s.top())
while s.isEmpty() is False:
    print(s.pop())

# print(s.isEmpty())

print(s.checkStack())

print(s.top())
print(s.size())