def shortest_substring(s, chars):
    char_count = dict.fromkeys(chars, 0)
    required = len(chars)
    formed = 0

    left, right = 0, 0
    min_length = float('inf')
    result = None

    while right < len(s):
        if s[right] in char_count:
            char_count[s[right]] += 1
            if char_count[s[right]] == 1:
                formed += 1
        
        while formed == required:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                result = s[left:right+1]
            
            if s[left] in char_count:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    formed -= 1
            
            left += 1
        
        right += 1
    return result if result is not None else 'null'