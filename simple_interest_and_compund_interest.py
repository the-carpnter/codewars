si = lambda p, r, n : p + p*r*n
ci = lambda p, r, n: ci(p + p*r, r, n - 1) if n else p

def interest(*a):
    return [round(si(*a)), round(ci(*a))]
