def print_nums(*a):
    k = len(str(max(a))) if a else 0
    return '\n'.join(map(lambda x: '0' * (k - len(str(x))) + str(x), a))
