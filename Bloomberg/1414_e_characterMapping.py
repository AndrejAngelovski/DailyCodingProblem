def is_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    
    mapping = {}
    for c1, c2 in zip(s1, s2):
        if c1 not in mapping:
            if c2 in mapping.values():
                return False
            mapping[c1] = c2
        elif mapping[c1] != c2:
            return False
    
    return True
