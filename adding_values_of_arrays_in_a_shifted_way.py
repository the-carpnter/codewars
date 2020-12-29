def sum_arrays(arrays, shift):
    a = []
    l = len(arrays)
    for i, x in enumerate(arrays):
        a += [i*shift*[0] + x + [0]*shift*(l-1-i)]
    return [*map(sum,zip(*a))]
