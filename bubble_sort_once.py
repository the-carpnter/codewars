def bubblesort_once(l):
    l = l.copy()
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            l[i], l[i+1] = l[i+1], l[i]
    return l
