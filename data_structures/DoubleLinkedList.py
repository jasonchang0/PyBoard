# LinkedList in Python -> Use collections.deque instead

from collections import deque

# construct a linkedlist using a string
dllst = deque('abcde')

# insert from the left
dllst.appendleft('a')

# insert from the right
dllst.append('f')

# remove from the front
dllst.popleft()

# remove from the right
dllst.pop()

# obtain the size of the deque
dllst.count

# conversion toArray
list(dllst)

# using deque for stack
for i in range(dllst.count):
    next_item = list(dllst)[-1]
    dllst.rotate(1)

# using deque for queue
for i in range(dllst.count):
    next_item = list(dllst)[0]
    dllst.rotate(-1)





    