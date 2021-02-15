def share_price(invested, changes):
    for i in changes:
        invested += invested * i * 0.01
    return '{:.2f}'.format(invested)
