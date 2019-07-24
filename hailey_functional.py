import collections
from functools import reduce

def is_sorted_wrt(s, p):
  p_hash = collections.defaultdict(lambda: None)
  for i in range(len(p)):
    p_hash[p[i]] = i

  s_index = map(lambda x: p_hash[x], s)
  s_index_filtered = filter(lambda x: x is not None, s_index)
  s_index_reduced = reduce(
      lambda s_tup, x: (s_tup[0] and s_tup[1] <= x, max(s_tup[1], x)), 
      s_index_filtered, 
      (True, 0)
      )
  
  return s_index_reduced[0]
