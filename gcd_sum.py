from math import gcd
def solve(s,g):
    if gcd(s-g, s) == g and s != g:
        return tuple(sorted([s-g, g]))
    return -1
