# Basic Typed Arraylist -> Used array.array

import array

# instantiate a typed array with datatype and list of data
arr = array.array('d', [1.5, 2.5, 3.5, 4.5])

# add element to the back of the array
arr.append(5.5)

# insert element at specific index
arr.insert(0, 0.5)

# remove element at specific index
arr.pop(4)

# remove element if present in the array
arr.remove(5.5)

# get the specific datatype of the entire array
arr.typecode



