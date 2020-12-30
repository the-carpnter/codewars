def vowel_one(s):
    return ['0','1'][s[0].lower() in 'aeiou'] + vowel_one(s[1:]) if s else ''
