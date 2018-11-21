def verify(p, k):
    if p == 0:
        return True

    return (p-1)*p**(k-1) == (p-1)**k


for p in range(100):
    for k in range(100):
        if verify(p, k):
            print('p:{}, k:{}'.format(p, k))


