def vert_mirror(strng):
    return '\n'.join(map(lambda x:x[::-1], strng.split('\n')))
def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1]) 
def oper(fct, s):
    return fct(s)
