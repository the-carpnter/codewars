def balanced_num(number):
    n = str(number)
    l = len(n)//2
    if len(n)%2==0:
        x, y = sum(map(int,n[:l-1])), sum(map(int,n[l+1:]))
    else:
        x, y = sum(map(int,n[:l])), sum(map(int,n[l+1:]))
    return 'Balanced' if x == y else 'Not Balanced'
