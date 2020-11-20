def factorial(n, x=1, fact=1):
    if n in {0,1} or x > n:
        return fact
    return factorial(n, x+1, fact*x)
