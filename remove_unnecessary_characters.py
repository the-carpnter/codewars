f = lambda x: x[-1:-3:-1] + '.' + x[-3::-1] + '$'
def remove_char(array):
    return [f(x)[::-1] for x in [''.join(k for k in i if k.isnumeric()) for i in array]]
