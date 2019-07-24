def is_sorted_wrt(s, p):
  a=[c for c in map(p.find,s)if-1<c];return a==sorted(a)
