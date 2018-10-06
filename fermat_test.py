import random


def gcd(x, y):
    # print('x: {}, y: {}'.format(x, y))
    if y == 0:
        return x

    return gcd(y, x % y)


def fermat_test(n):
    if n < 2:
        return False

    a = random.randint(2, n)

    if gcd(a, n) != 1:
        return False
    elif int(a ** (n - 1)) % n != 1:
        return False

    return True


def fermat_theorem(a, n):
    if a == 0 or n == 0:
        return

    return (int(a ** (n - 1))) % n


# for a in range(100):
#     for n in range(100):
#         if a > 0 and fermat_test(n):
#             print('a: {}, n: {}'.format(a, n))
#             print(fermat_theorem(a, n))

n = 10000
for a in range(n):
    # print(gcd(15, a))=
    if fermat_theorem(a, n) == 1:
        print('a_f: {}, n_f: {}'.format(a, n))

    elif gcd(n, a) == 1:
        print('a: {}, n: {}'.format(a, n))
        print(fermat_theorem(a, n))


# print(gcd(5, 10))
