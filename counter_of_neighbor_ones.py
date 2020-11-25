def ones_counter(input):
    return [len(i) for i in ((''.join(map(str, input))).replace('0',' ')).split(' ') if i != '']
