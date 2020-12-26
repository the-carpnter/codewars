def get_missing_element(seq):
    for i, x in enumerate(sorted(seq)):
        if i != x:
            return x - 1
    return x + 1
