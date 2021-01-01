def string_chunk(string, n = 0, i = 0):
    return [string[i: i + n]] + string_chunk(string, n, i + n) if string[i:] and type(n) is int and n > 0 else []
