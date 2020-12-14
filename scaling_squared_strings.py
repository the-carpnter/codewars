def scale(s, k, n):
    if s:
        return '\n'.join('\n'.join([i]*n) for i in [''.join(map(lambda x: x*k, i)) for i in s.split('\n')])
    return ''
