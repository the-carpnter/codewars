def is_bouncy(n):
    return [*str(n)] != sorted(str(n), reverse = True) and [*str(n)] != sorted(str(n))
