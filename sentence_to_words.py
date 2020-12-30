def splitSentence(s, j = 0, i = 0):
    if i < len(s):
        return [s[j : i]] + splitSentence(s, i + 1, i + 1) if s[i] == ' ' else splitSentence(s, j, i + 1)
    return [s[j : ]]
