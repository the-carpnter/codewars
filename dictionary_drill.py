def user_contacts(data):
    k = {}
    for i in data:
        try:
            x, y = i
            k[x] = y
        except ValueError:
            k[i[0]] = None        
    return k
