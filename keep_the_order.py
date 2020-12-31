def keep_order(a, val, i=0):
    if a:
        return i if val <= a[0] else keep_order(a[1:], val, i+1)
    return i
