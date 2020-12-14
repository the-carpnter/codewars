def reverse_slice(s):
    return [s[::-1]] + reverse_slice(s[:-1]) if s else []
