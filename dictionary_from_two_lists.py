from itertools import zip_longest
def createDict(keys, values):
    return {key: value for key, value in zip_longest(keys, values) if key}
