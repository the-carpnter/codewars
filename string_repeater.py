def repeater(string, n):
    return repeater(string, n-1) + string if n else ''
