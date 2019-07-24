def is_sorted_wrt(s, p):
    i = [p.index(x) for x in s if x in p]
    return sorted(i) == i
