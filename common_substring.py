def substring_test(s1, s2):
    if s1 and s2 and len(s1) > 1:
        return True if s1[:2].lower() in s2.lower() else substring_test(s1[1:], s2)
    return False
