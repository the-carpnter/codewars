def convert_bits(a, b):
    a = bin(a)[2:].zfill(32)
    b = bin(b)[2:].zfill(32)
    return sum(1 for x,y in zip(a,b) if x != y)
