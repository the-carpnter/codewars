def solution(st, limit, i=0):
    if i == len(st):
        return ''
    if i == limit:
        return '...'
    return st[i] + solution(st, limit, i+1)
