def remove(s):
    count, k = 0, ''
    for i in s:
        if i != '!':
            k += i
        else:
            count += 1
    return k + '!'*count  
