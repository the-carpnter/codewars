def get_issuer(number):
    n = str(number)
    if (n.startswith('34') or n.startswith('37')) and len(n) == 15:
        return 'AMEX'
    if n.startswith('6011') and len(n) == 16:
        return 'Discover'
    if n[:2] in {'51','52', '53', '54', '55'} and len(n) == 16:
        return 'Mastercard'
    if n.startswith('4') and len(n) in {13, 16}:
        return 'VISA'
    return 'Unknown'
