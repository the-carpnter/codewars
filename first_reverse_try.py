def first_reverse_try(a):
    try:
        a[0], a[-1] = a[-1], a[0]
        return a
    except IndexError:
        return []
