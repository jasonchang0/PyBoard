#Sets in Python -> Use built - in set

# instantiate a set manually
s1 = {1, 2, 3, 4, 5, 5, 3, 3, 2, 3, 1}

# instantiate a set using a iterable
s2 = set(''.join(map(str, s1)))

# find the intersection of two sets
s1.intersection(s2)

# find the union of two sets
s1.union(s2)

# find the difference between two sets -> s1.union(s2) - s1.intersection(s2)
s1.difference(s2)

# find if two sets are equivalent
s1.issubset(s2) and s1.issuperset(s2)

# create a copy of a set
s1.copy()

# clear the entire set
s1.clear()

# add element to the set
s1.add(6)

# remove element from the set
try:
    s1.remove(7)
except KeyError as e:
    raise KeyError('Element not found in the set')





