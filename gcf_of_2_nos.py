def find_GCF(a, b):
    if a == b:
        return a
    return find_GCF(a - b, b) if a > b else find_GCF(a, b - a)
