from itertools import cycle
def encode(message, key):
    return [*map(lambda x,y: x+y, map(lambda x: ord(x) - 96, message), cycle(map(int, str(key))))]
