def growing_plant(upSpeed, downSpeed, desiredHeight, dn = 0, height = 0, day = 1):
    if height >= desiredHeight:
        return day
    if dn == 0:
        height += upSpeed
        dn = 1
        return growing_plant(upSpeed, downSpeed, desiredHeight, dn, height, day)
    if dn == 1:
        height -= downSpeed
        dn = 0
        day += 1
        return growing_plant(upSpeed, downSpeed, desiredHeight, dn, height, day)
