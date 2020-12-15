def mean(lst):
    return [sum(int(i) for i in lst if i.isnumeric())/10, ''.join(i for i in lst if i.isalpha())]
