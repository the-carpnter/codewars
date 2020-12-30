def distribute(m, n):
    if n == 0:
        return []
    if m <= 0:
        return [0] * n
    x, y = m//n, m%n
    return (n - y)*[x] + y*[x+1] if y != 0 else n * [x]
