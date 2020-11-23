def partlist(arr):
    k = []
    i = 0
    while i != len(arr) - 1:
        k += [(' '.join(arr[:i+1]), ' '.join(arr[i+1:]))]
        i += 1
    return k
