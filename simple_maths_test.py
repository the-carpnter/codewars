from gmpy2 import is_prime
def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]
