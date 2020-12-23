from functools import reduce
def eq_sum_powdig(n, e):
    return [i for i in range(2, n + 1) if reduce(lambda x, y: x + y ** e, map(int, str(i)), 0) == i]
