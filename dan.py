# coding=utf-8

import re
 
class DanProgrammingChallenge2(object):
  """Class."""
 
  def __init__(self, s = None, p=None):
    self.s = s
    self.p = p
    self.output = self.process()
 
  def process(self):
    result = False
    if not self.s or not self.p:
      result = True
      return result
    np = '[^' + self.p + ']' # Not p
 
    news = re.sub(np, '', self.s) # New s
    nsl = list(news)
    for c in self.p:
      while len(nsl) > 0 and nsl[0] == c:
        nsl.pop(0)
    if len(nsl) == 0:
      result = True
    return result
 
def pc2_dan(s, p):
  sort_obj = DanProgrammingChallenge2(s, p)
  return sort_obj.output
 
is_sorted_wrt = pc2_dan
