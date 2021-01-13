heggeleggleggo = lambda word: word[0] + ['egg', ''][word[0].lower() in 'aeiou '] + heggeleggleggo(word[1:]) if word else ''
