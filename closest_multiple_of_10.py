def closest_multiple_10(i):
    return [(i//10)*10,(i//10+1)*10][i%10 >= 5] if i%10 else i
