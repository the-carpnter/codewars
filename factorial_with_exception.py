def factorial(n):
    if n not in range(0,13):
        raise ValueError('n out of desired range')
    return n*factorial(n-1) if n else 1
