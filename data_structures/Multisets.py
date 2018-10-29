# Multisets in Python -> Use collections.Counter

from collections import Counter

# instantiate a new Counter
inventory = Counter()

# import information from dictionary into the Counter object
quant_dict = {'bread': 1, 'egg': 2, 'milk': 3}
inventory.update(quant_dict)

# number of unique elements in the multiset
len(inventory)

# number of total elements in the multiset
sum(inventory.values())

# access each element in similar manner as dictionary
bread = inventory['bread']





