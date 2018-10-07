# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_Occur(S, Char):
    return [i for i, letter in enumerate(s) if letter == Char]


def solution(S, K):

    # write your code in Python 3.6
    num_dash = len(find_Occur(S, '-'))
    S.replace('-', '')

    num_char = len(S) - num_dash
    num_head = len(S) % K
    num_subset = len(S) // K

    output = ''

    for _ in range(num_subset):
        if not _:
            output += S[:num_head]

        output += S[K*(_-1) + num_head: K*(_) + num_head]

    return output



