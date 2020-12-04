def vowel_indices(word, i=0):
    if i == len(word):
        return []
    if word[i].lower() in 'aeiouy':
        return [i+1] + vowel_indices(word, i+1)
    return vowel_indices(word, i+1)
