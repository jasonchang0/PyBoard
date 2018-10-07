# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def find_Occur(lst, val):
    return [index for index, x in enumerate(lst) if x == val]


def solution(stores, houses):
    try:
        assert isinstance(stores, list) and isinstance(houses, list)

    except AssertionError as e:
        stores = []
        houses = stores
        print('Incorrect input type given.')

    output = []

    if not len(stores) or not len(houses):
        return output

    for house in houses:
        d_stores = [abs(s - house) for s in stores]

        min_dis = min(d_stores)
        n_near_store = d_stores.count(min_dis)

        if n_near_store == 1:
            nearest_store = d_stores.index(min_dis)

        elif n_near_store > 1:
            '''
            If many stores are equidistant from a particular house,
            choose the store with the smallest numerical location.
            '''
            equidis = find_Occur(d_stores, min_dis)

            min_loc = sys.maxsize
            nearest_store = 0

            '''
            Since it's only the location that matters as output,
            in case that there are multiple stores with the same
            location, we simply return location of the first incident.
            '''
            for s in equidis:
                if (stores[s] < min_loc):
                    min_loc = stores[s]
                    nearest_store = s

        output += [stores[nearest_store]]

    assert len(output) == len(houses)
    return output



