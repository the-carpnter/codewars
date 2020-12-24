def remove_vowels(s):
    if s:
        x, *xs = s
        return x + remove_vowels(xs) if x not in 'aeiou' else remove_vowels(xs)
    return ''
