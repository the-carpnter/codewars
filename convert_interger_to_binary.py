def to_binary(n):
    return bin(n)[2:] if n >= 0 else bin(2**32 + n)[2:]
