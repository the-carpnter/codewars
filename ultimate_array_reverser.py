def reverse(a):
    x = ''.join(a)[::-1]
    k = []
    j = 0
    for word in a:
        k += [x[j: j + len(word)]]
        j += len(word)
    return k  
