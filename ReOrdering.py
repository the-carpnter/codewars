def re_ordering(text):
    k = []
    for word in text.split():
        if word[0].isupper():
            k.insert(0, word)
        else:
            k += [word]
    return ' '.join(k)
