def check_vowel(s, i):
    try:
        return s[i].lower() in 'aeiou'
    except IndexError:
        return False   
