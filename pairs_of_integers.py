from itertools import product
def generate_pairs(n):
    return [[x,y] for x,y in product(range(n+1), repeat = 2) if x <= y]
