rev = lambda n: int(str(n)[::-1])

def reverse_invert(lst):
    k = []
    for x in lst:
        if type(x) is int:
            k += [rev(abs(x)) * [1, -1][x > 0]]
    return k
