def ext_gcd(x, y):

    if y == 0:
        print(x, 1, 0)
        return x, 1, 0

    else:
        d, a, b = ext_gcd(y, x % y)
        print("x: {}, y: {}".format(x, y))
        print("x//y: {}".format(x // y))
        print(d, b, a - (x // y)*b)
        return d, b, a - (x // y)*b


print(ext_gcd(11, 6))
