def cube_sum(n, m):
    if n == m:
        return 0
    return n**3 + cube_sum(n-1, m) if n > m else m**3 + cube_sum(n, m-1)
