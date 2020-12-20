from itertools import combinations
def digits(num):
    return [sum(map(int,i)) for i in combinations(str(num),2)]
