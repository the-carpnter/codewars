import string
def consonant_count(s):
    return sum(i not in 'aeiou' for i in s.lower() if i in string.ascii_lowercase)
