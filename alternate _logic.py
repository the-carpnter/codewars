from functools import reduce
def alt_or(lst):
    return reduce(lambda x,y: x or y, lst) if lst else None
