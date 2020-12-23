def round_to_five(n):
    return [*map(lambda x: int(x) // 5 * 5 + (x - int(x) // 5 * 5 >= 2.5) * 5, n)]
