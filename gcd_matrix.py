gcd = lambda a,b : gcd(b, a%b) if b else a
def gcd_matrix(a,b):
    return round(sum(gcd(x,y) for x in a for y in b) / (len(a) * len(b)), 3)
