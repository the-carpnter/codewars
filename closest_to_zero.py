def closest(lst):
    a = sorted(lst, key = abs)
    if a[0] and -a[0] in a[1:]: 
        return None
    return a[0]
