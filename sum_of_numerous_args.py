def find_sum(*args):
    return sum(args) if all(x>=0 for x in args) else -1
