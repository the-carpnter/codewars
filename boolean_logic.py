def func_or(a,b):
    return bool(a) or bool(b)

def func_xor(a,b):
    return (bool(a) and not b) or (bool(b) and not a)
