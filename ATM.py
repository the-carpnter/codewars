def solve(n):
    if n == 0:
        return 0
    if n % 10:
        return -1
    for x in [500, 200, 100, 50, 20, 10]:
        if n >= x:
            return 1 + solve(n - x)
