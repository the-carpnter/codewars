ef count_animals(sentence):
    return sum([int(i) for i in sentence.split() if i.isnumeric()])
