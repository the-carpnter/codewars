def speedify(st): 
    k = []
    for i, c in enumerate(st):
        pos = i + ord(c.lower()) - 97
        if pos >= len(k):
            k += [' ']*(pos - len(k)) + [c]
        k[pos] = c
    return ''.join(k)
