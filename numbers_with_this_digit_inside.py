def numbers_with_digit_inside(x, d, i=1, c=0, s=0, p=0):  
    while True:
        if str(d) in str(i):
            c += 1
            s += i
            if p:
                p = p*i
            else:
                p = i
        if i == x:
            return [c, s, p]
        i += 1
