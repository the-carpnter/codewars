def shuffle_it(a, *args):
    for arg in args:
        x, y = arg
        a[x], a[y] = a[y], a[x]
    return a
