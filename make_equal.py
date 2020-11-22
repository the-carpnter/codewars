def count(a, t, x):
    re = 0
    while a:
        n = a.pop(0)
        if x and abs(n-t) % x == 0 or n == t:
            re += 1
    return re
