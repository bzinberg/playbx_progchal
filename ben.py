def is_sorted_wrt(s, p):
  ranks = {ch: i for (i, ch) in enumerate(p)}
  sRanks = (ranks[ch] for ch in s if ch in ranks)
  return all(i <= j for (i, j) in consecutivePairs(sRanks))

def consecutivePairs(seq):
  """Yields all pairs of consecutive elements of `seq`, in order."""
  seq = iter(seq)
  try:
    prev = next(seq)
  except StopIteration:
    return
  for x in seq:
    yield (prev, x)
    prev = x
