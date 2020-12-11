def sum(*args):
    i, re = 0, 0
    while True:
        try:
            if type(args[i]) is int:
                re += args[i]
        except IndexError:
            return re
        i += 1
