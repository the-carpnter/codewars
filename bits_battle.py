def bits_battle(numbers):
    odds = ''
    evens = ''
    for x in numbers:
        if x % 2:
            odds += bin(x)[2:]
        else:
            evens += bin(x)[2:]
    odc = odds.count('1')
    evc = evens.count('0')
    if odc > evc:
        return 'odds win'
    if odc < evc:
        return 'evens win'
    return 'tie'
