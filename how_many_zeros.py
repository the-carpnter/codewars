def countzero(s, count=0):
    if s:
        if s[0] in 'abdegopq069DOPQR':
            count += 1
        if s[0] in '%&B8':
            count += 2
        if s[0:2] == '()':
            count += 1
            s = s[1:]
        return countzero(s[1:], count)
    return count 
