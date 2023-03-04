# Given a mapping of digits to letters (as in a phone number), and a digit string,
# return all possible letters the number could represent. You can assume each valid
# number in the mapping is a single digit.

# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should
# return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

def letter_combinations(digits, mapping):
    if not digits:
        return []
    
    def backtrack(index, path):
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        
        for letter in mapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    res = []
    backtrack(0, [])
    return res

mapping = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

digits = input("Enter a digit string: ")
combinations = letter_combinations(digits, mapping)
print(combinations)

# The letter_combinations function uses backtracking
# to generate all possible letter combinations. 
# The backtrack function takes an index into the digit
# string and a path of letters generated so far. It tries
# appending each possible letter for the current digit to
# the path, and then recursively backtracking to try the
# next digit. If the path is the same length as the digit
# string, the function has found a valid combination 
# and adds it to the result list.