def to_acronym(input):
    return ''.join(map(lambda x: x[0].upper(), input.split()))
