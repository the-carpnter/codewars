def bin_8(n):
    x = bin(n)[2:]
    return (8 - len(x))*'0' + x

def word_to_bin(word):
    return [*map(bin_8, map(ord, word))]
