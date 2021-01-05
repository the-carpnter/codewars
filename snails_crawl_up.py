def snail(column, day, night):
    d = 1
    while True:
        column -= day
        if column <= 0:
            return d
        column += night
        d += 1
