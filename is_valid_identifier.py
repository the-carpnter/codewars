import string
def is_valid(idn): 
    return (idn[0] in string.ascii_letters or idn[0] in '_$') and all(i in set(string.ascii_letters + '_$' + '0123456789') for i in idn) if idn else False
