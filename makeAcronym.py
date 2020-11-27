def make_acronym(phrase):
    try:
        if all(i.isalpha() or i == ' ' for i in phrase):
            phrase = phrase.split()
            return ''.join(i[0].upper() for i in phrase)
        else:
            return 'Not letters'
    except:
        return 'Not a string'
