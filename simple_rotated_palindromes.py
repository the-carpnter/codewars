def solve(st, count=1):
    st = st[-1] + st[:-1]
    if st == st[::-1]:
        return True
    if count == len(st) - 1:
        return False
    return solve(st, count+1)
