def last(*args):
    try:
        return args[-1][-1]
    except TypeError:
        return args[-1]
