from functools import reduce
def calculate_total(t1, t2):
    t1s=reduce(lambda a,b: a+b,t1,0)
    t2s=reduce(lambda a,b: a+b,t2,0)
    return t1s>t2s
