def move_vowels(input): 
    return ''.join(i for i in input if i not in 'aeiou') + ''.join(i for i in input if i in 'aeiou')
