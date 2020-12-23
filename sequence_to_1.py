signum = lambda n: -1 if n > 0 else 1
def seq_to_one(n):
    return [*range(n, 1 + signum(n), signum(n))]
