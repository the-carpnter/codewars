pattern = lambda n : pattern(n - 1) + '\n' + '1' + '*'*(n - 1) + str(n)  if  n > 1 else '1'
