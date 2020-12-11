def friend(x):
    if x:
        return [x[0]] + friend(x[1:]) if len(x[0])==4 else friend(x[1:])
    return []
