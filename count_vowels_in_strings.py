def count_vowels(s = ''):
    try:
        return sum(1 for i in s.lower() if i in 'aeiou')
    except AttributeError:
        return None
