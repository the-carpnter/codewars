def tower_combination(n):
    return n * tower_combination(n-1) if n else 1
