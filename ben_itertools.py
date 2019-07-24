import itertools
zip = itertools.izip if hasattr(itertools, 'izip') else zip  # for Python 2/3


def is_sorted_wrt(s, p):
  ranks = {ch: i for (i, ch) in enumerate(p)}
  sRanks = (ranks[ch] for ch in s if ch in ranks)
  return all(i <= j for (i, j) in consecutivePairs(sRanks))


def consecutivePairs(seq):
  firsts, seconds = itertools.tee(seq)
  next(seconds, None)
  return zip(firsts, seconds)
