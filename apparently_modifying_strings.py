def apparently(string):
    text = []
    *string, = string.split()
    for i, x in enumerate(string):
        text += [x]
        if (x == 'and' or x == 'but'):
            try:
                if string[i+1] != 'apparently':
                    text += ['apparently']
            except IndexError:
                text += ['apparently']
            
    return ' '.join(text)
