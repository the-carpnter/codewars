def reverse_it(data):
    x = type(data)
    if x in (list, tuple, set, dict):
        return data
    return x(str(data)[::-1])
