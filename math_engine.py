from functools import reduce
def math_engine(arr):
    return sum(filter(lambda x: x<0, arr)) + reduce(lambda x,y: x*y, filter(lambda x: x>=0, arr), 1) if arr is not None else 0
