f = lambda x: ['Open', 'Senior'][x[0]>=55 and x[1]>7]
def open_or_senior(data):
    return [*map(f, data)]
