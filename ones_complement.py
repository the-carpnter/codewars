def ones_complement(b):
    return ones_complement(b[:-1]) + ['1', '0'][b[-1] == '1'] if len(b) >= 1 else ''
