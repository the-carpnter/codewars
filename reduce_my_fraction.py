from math import gcd
def reduce_fraction(fraction):
    x, y = fraction
    r = gcd(*fraction)
    return x//r, y//r
