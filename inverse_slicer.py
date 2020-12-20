def inverse_slice(items, a, b):
    return [*filter(lambda x: items.index(x) not in range(a,  b), items)]
