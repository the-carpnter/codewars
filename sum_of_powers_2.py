def powers(n):
    k = []
    while n:
        n, m = divmod(n, 2)
        k += [m]
    return [2**i for i,v in enumerate(k) if v != 0]
