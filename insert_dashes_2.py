digits = lambda n: digits(n//10) + [n%10] if n else []
def insert_dash2(num):
    n = digits(num)
    def helper(a):
        if a:
            x, *xs = a
            if x and xs and xs[0] and (x + xs[0]) % 2 == 0:
                if x % 2 == 0:
                    return [str(x), '*'] + helper(xs)
                else:
                    return [str(x), '-'] + helper(xs)
            return [str(x)] + helper(xs)
        return []
    return '0'if num == 0 else ''.join(helper(n))   
