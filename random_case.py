from random import getrandbits as rb
f = lambda x: [str.upper, str.lower][x]
def random_case(x):
    return f(rb(1))(x[0]) + random_case(x[1:]) if x else ''
