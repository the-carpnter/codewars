def squares(x, n):
    if n <= 0:
        return []
    return [x] + squares(x**2, n-1)
