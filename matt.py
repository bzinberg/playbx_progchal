# Builds a map of indexes for each character
# in char_order and then uses that to
# validate the order in the text.
# Performance is O(n) where n is the combined
# length of text + char_order. 
def is_sorted_wrt(text, char_order):
  # Split apart char_order into a dictionary
  # containing char:index where index is the
  # 0-based index of the character in the
  # string.
  # NOTE: Because the char_order values in
  # the unit tests are all short this is only
  # slightly faster than calling
  # char_order.find() directly.
  order_dict = {}

  ## Method 1: Zip + dict (0.71 for 10k)
  # order_dict = dict(zip(
  #     char_order, range(len(char_order))))

  ## Method 2: Enumerate (0.50 for 10k) 
  # for num, char in enumerate(char_order):
  #   order_dict[char] = num

  ## Method 3: While loop (0.45 for 10k)
  num = 0
  while num < len(char_order):
    order_dict[char_order[num]] = num
    num += 1

  # Perform the method lookup once here
  # instead of in each iteration of the loop.
  lookup_order = order_dict.get

  # Iterate through the text and make sure
  # that the characters are in the expected
  # order.
  last_order = -1
  for char in text:
    order = lookup_order(char, -1)
    if order != -1:
      if order < last_order:
        return False
      last_order = order
  return True
