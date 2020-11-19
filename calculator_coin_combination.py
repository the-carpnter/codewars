def coin_combo(cents):
    k = []
    for i in [25, 10, 5, 1]:
        if i > cents:
            k += [0]
        elif i < cents:
            cents, m = divmod(cents, i)
            k += [cents]
            cents = m
        elif i == cents:
            k += [1]
            cents = 0
    return k[::-1]
