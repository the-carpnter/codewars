from math import log
def manipulate(n):
    return n // 10**(x := int(log(n, 10)) // 2 + (log(n, 10) % 1 != 0)) * 10**x if n > 9 else 0
