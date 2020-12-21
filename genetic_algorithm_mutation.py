d = {'0': '1', '1': '0'}
def mutate(c, p):
    i = int(len(c) * p)
    return ''.join(map(lambda x: d[x], c[:i])) + c[i:]
