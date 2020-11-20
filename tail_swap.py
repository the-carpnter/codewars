def tail_swap(strings):
    a, b = strings
    x1, y1 = a.split(':')
    x2, y2 = b.split(':')
    return [x1+':'+y2, x2+':'+y1]
