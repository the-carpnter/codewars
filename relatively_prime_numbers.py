def gcd(a, b):
    return gcd(b, a%b) if b else a

def relatively_prime (n, l):
    return [*filter(lambda x: gcd(x,n)==1, l)]
