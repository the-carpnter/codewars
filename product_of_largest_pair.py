def max_product(a):
    x, y = (a[0], a[1]) if a[0] < a[1] else (a[1], a[0])
    for i in a[2:]:
        if i > x:
            x = i
        if i > y:
            x, y = y, x
    return x * y
