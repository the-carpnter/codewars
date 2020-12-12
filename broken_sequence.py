def find_missing_number(seq):
    if not seq:
        return 0
    try:
        a = sorted(map(int, seq.split(' ')))
        try:
            return [i for i in range(1, max(a)+1) if i not in a][0]
        except IndexError:
            return 0
    except ValueError:
        return 1   
