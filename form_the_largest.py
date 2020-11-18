def max_number(n):
    return int(''.join(sorted(str(n), key = int, reverse = True)))
