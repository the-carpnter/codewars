def multiples(s1,s2,s3):
    k = []
    while s3:
        s3 -= 1
        if s3 and s3%s1 == 0 and s3%s2 == 0:
            k.insert(0, s3)
    return k 
