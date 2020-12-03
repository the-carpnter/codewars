def averages(a):
    return [(a[0] + a[1])/2] + averages(a[1:]) if a and len(a)>1 else []
