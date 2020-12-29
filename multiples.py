def multiple(x):
    k = ''
    if x % 3 == 0:
        k += 'Bang'
    if x % 5 == 0:
        k += 'Boom'
    return k if k else 'Miss'
