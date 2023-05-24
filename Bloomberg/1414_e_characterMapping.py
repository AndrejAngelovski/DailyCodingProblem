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

"""
The function is_isomorphic takes two input strings, s1 and s2. It checks if the lengths of the strings are equal, returning False if they are not, as unequal length strings cannot have a one-to-one character mapping.

We initialize an empty dictionary, mapping, to keep track of the character mapping from s1 to s2.

The zip function combines s1 and s2 and returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, the second item in each passed iterator is paired together, and so on.

The for loop iterates over this zip object. For each pair of characters c1 from s1 and c2 from s2:

If c1 is not already in mapping (i.e., we haven't seen this character in s1 before):
If c2 is already a value in mapping, this means that a previous character in s1 has been mapped to c2. Hence c1 cannot be mapped to c2, and the function returns False.
Otherwise, we add the mapping from c1 to c2 to mapping.
If c1 is already in mapping, we check if it was previously mapped to the same character c2. If not, the function returns False.
If none of the checks have returned False by the end of the loop, then s1 and s2 are isomorphic, and the function returns True.
"""