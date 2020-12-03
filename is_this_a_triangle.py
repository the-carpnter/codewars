from itertools import permutations
def is_triangle(a, b, c):
    for x,y,z in permutations([a,b,c]):
        if x >= y + z:
            return False
    return True
