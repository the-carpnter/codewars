def archers_ready(archers):
    for x in archers:
        if x < 5:
            return False
    return True if archers else False
