def sentencify(words):
    return words[0][0].upper() + words[0][1:] + ' ' + ' '.join(words[1:]) + '.' if words and len(words) > 1 else words[0].title() + '.'
