def procedure(i, x = 1):
    return sum(map(int,str(x*i))) + procedure(i, x + 1) if x*i <= 100 else 0
