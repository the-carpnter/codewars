def missing_values(seq):
    re = 1
    for x in set(seq):
        if seq.count(x) == 1:
            re *= x * x
        if seq.count(x) == 2:
            re *= x
    return re
