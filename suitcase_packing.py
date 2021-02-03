 def fit_in(a,b,m,n):
    return m*n >= a**2 + b**2 and (a + b) <= max(m, n) and a <= min(m, n) and b <= min(m,n)
