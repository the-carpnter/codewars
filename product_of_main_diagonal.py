from functools import reduce
def main_diagonal_product(mat):
    return reduce(lambda x,y: x*y, [r[i] for i, r in enumerate(mat)])
