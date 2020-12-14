def is_narcissistic(i):
    n, x = i, len(str(i))
    sum = 0
    while n:
        n, m = divmod(n, 10)
        sum += m**x
    return sum == i
