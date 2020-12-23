f = lambda n: n * f(n - 1) if n > 0 else 1
def sum_factorial(lst):
    return sum(map(f, lst))
