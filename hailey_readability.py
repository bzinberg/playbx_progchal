import collections

def is_sorted_wrt(s, p):
  p_hash = collections.defaultdict(lambda: None)
  for i in range(len(p)):
    p_hash[p[i]] = i

  s_index = [p_hash[x] for x in s if p_hash[x] is not None]
  prev_n = 0
  for n in s_index:
    if n < prev_n:
      return False
    prev_n = n
  
  return True
