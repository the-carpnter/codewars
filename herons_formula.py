from functools import reduce
def heron(*a):
    s = sum(a)/2
    return round(reduce(lambda x, y : x * y, [s - i for i in a], s)**0.5, 2)
