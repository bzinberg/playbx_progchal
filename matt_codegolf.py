from functools import reduce

# This earns readability demerits, but on the plus side it uses map/reduce and
# can split up the job to run as multiple processes to handle large data sets.
# It is not as efficient as my other solution since it fully iterates through
# the text twice (once to map and once to reduce) and uses String.find() to
# scan char_order to find the index. But, it could easily be updated to use a
# dictionary as in my other solution. 

def is_sorted_wrt(text, char_order): 
  return reduce(lambda max, cur: max if max is None or cur == -1 else (cur if cur >= max else None), map(char_order.find, text), -1) is not None
