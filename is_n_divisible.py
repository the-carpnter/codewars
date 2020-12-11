def is_divisible(*a):
    return all(a[0]%i == 0 for i in a[1:])
