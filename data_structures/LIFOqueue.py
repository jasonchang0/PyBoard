# LIFO (Last-In, First-Out) queue -> use queue.LifoQueue

from queue import LifoQueue

# instantiate an empty queue
# If maxsize is less than or equal to zero, the queue size is infinite.If maxsize is
# less than or equal to zero, the queue size is infinite.
q = LifoQueue(maxsize=-1)

# put elements into the queue
q.put('breakfast')
q.put('lunch')
q.put('dinner')

# push elements out of the queue
q.get()

# check if the queue is empty
q.empty()

# get the size of the queue
q.qsize()


