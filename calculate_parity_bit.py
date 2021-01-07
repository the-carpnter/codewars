def check_parity(parity, bin_str): 
    if bin_str.count('1') % 2:
        return [0, 1][parity == 'even']
    return [1, 0][parity == 'even']
