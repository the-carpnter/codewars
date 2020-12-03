def nthterm(a, n, c):
    return a if n==0 else nthterm(a+c, n-1, c)
