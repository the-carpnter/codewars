from functools import reduce
def unused_digits(*a):
    return ''.join(i for i in '0123456789' if i not in set(reduce(lambda x, y: str(x) + str(y), a, '')))   
