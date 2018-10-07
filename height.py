# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    try:
        assert isinstance(A, list)

    except AssertionError as e:
        A = []
        print('Incorrect input type given.')

    A_max = 0
    count = 0

    '''
    New row is only created when we encounter a new max
    in heigher (or a val equal to the old max), such that
    no row fits this new max.
    '''

    if not len(A):
        return count

    for val in A:
        if val >= A_max:
            A_max = val
            count += 1

    return count





