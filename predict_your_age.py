from functools import reduce
def predict_age(*a):
    return reduce(lambda x,y: x + y**2, a, 0)**0.5 // 2
