from math import pow
def find_next_power(val, n):
    return (int(pow(val, 1/n)) + 1)**n
