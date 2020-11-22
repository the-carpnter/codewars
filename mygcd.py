def mygcd(x,y):
    return mygcd(y%x, x) if x else y
