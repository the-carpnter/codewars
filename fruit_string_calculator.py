def calculate(string):
    op = ''
    k = []
    for i in string.split():
        try:
            if i == 'loses':
                op = '-'
            k += [int(i)]
        except:
            continue
    if op == '-':
        return k[0] - k[1]
    else:
        return k[0] + k[1]
