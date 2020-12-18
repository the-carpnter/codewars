def remove(s):
    k = ''
    for i, c in enumerate(s):
        if c != '!':
            k += c
        if c == '!' and all(x=='!' for x in s[i:]):
            k += '!'
    return k
