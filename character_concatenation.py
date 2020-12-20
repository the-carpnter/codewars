def char_concat(word, i=0):
    return word[i] + word[-1-i] + str(i+1) + char_concat(word, i+1) if 2*i + 1 < len(word) else ''
