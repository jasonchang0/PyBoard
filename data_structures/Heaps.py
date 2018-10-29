# Priority Queue/Min Heaps -> use queue.PriorityQueue

from queue import PriorityQueue

# instantiate a min heap
q = PriorityQueue()

# populate the PQ with (priority, element) pairs
q.put((4, 'school'))
q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

# iterate through the entire PQ with ascending priority
while not q.empty():
    next_item = q.get()
print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')
# (4, 'school')

