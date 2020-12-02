def namelist(names):
    k = []
    for i in names:
        k += [i['name']]
    if not k:
        return ''
    if len(k) == 2:
        return ' & '.join(k)
    if len(k) == 1:
        return k[0]
    return ', '.join(k[:-1]) + ' & ' + k[-1]
