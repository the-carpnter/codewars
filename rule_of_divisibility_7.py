def seven(m, steps=0):
    if len(str(m)) <= 2:
        return m, steps
    return seven(int(str(m)[:-1]) - 2*int(str(m)[-1]), steps+1)
