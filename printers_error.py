def printer_error(s):
    return str(len([i for i in s if i in 'nopqrstuvwxyz'])) + '/' + str(len(s))
