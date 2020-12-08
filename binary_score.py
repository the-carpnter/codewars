from math import log2
def score(n):
    return 2**(int(log2(n))+1) - 1 if n else 0
