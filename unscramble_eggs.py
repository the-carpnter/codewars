def unscramble_eggs(word):
    if word:
        if word[:3] != 'egg':
            return word[0] + unscramble_eggs(word[1:])
        return unscramble_eggs(word[3:])
    return ''
