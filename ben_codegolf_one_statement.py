def is_sorted_wrt(s, p):
  return(lambda a:a==sorted(a))([c for c in map(p.find,s)if-1<c])
