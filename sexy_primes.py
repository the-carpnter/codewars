from gmpy2 import is_prime
def sexy_prime(x, y):
    return is_prime(x) and is_prime(y) and abs(y - x) == 6
