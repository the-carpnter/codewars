def palindrome(num):
    try:
        if num < 0:
            raise TypeError
        k = []
        while num:
            num, m = divmod(num, 10)
            k.insert(0,m)
        return k == k[::-1]
    except TypeError:
        return 'Not valid'
