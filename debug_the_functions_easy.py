def multi(l_st):
    return l_st[0] * multi(l_st[1:]) if l_st else 1
def add(l_st):
    return l_st[0] + add(l_st[1:]) if l_st else 0
def reverse(string):
    return string[::-1]
