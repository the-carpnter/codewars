def split_the_bill(x):
    avg = sum(x.values()) / len(x)
    return {i: x[i] - avg if avg%1 == 0 else round(x[i]-avg, 2) for i in x}
