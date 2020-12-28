from gmpy2 import is_prime
def odd_not_prime(n):
    sum = 0
    while n:
        sum += (n%2 and not is_prime(n))
        n -= 1
    return sum   
