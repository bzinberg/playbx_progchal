import collections

def is_sorted_wrt(s, p):
    p_hash = collections.defaultdict(lambda: None)
    for i in range(len(p)):
        p_hash[p[i]] = i
        
    current_index = 0
    for letter in s:
        p_index = p_hash[letter]
        if p_index is not None:
            if p_index < current_index:
                return False
            current_index = p_index if p_index > current_index else current_index
    return True
