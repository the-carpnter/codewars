from itertools import product
def generate_number(squad, n):
    if n not in squad:
        return n
    k = [int(str(x)+str(y)) for x,y in product(range(1,10), repeat = 2) if x + y == n and int(str(x)+str(y)) not in squad]
    try:
        return min(k)
    except ValueError:
        return None
