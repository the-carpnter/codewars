def factory(x):
    return lambda arr: [*map(lambda y: x*y, arr)]
