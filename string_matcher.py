def is_matching(st, st1, st2):
    st = st.lower()
    s = (st1+st2).lower()
    for i in st.replace(' ', ''):
        if st.count(i) != s.count(i):
            return False
    return True
