def add(*args):
    return sum(x*y for x,y in enumerate(args, 1))
