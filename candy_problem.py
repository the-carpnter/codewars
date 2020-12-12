def candies(s):
    return sum(map(lambda x: max(s)-x, s)) if s and len(s) > 1 else -1
