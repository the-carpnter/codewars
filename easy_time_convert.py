def time_convert(num):
    h = str(num//60)
    h = '0'*(2 - len(h)) + h if len(h) <= 2 else h
    m = str(num%60)
    m = '0'*(2 - len(m)) + m
    return h + ':' + m if num > 0 else '00:00'
