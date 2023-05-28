# Implement an efficient string matching algorithm.
# That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
# If the pattern is found, return the start index of its location. If not, return False.


# KMP(Knuth-Morris-Pratt) algorithm - used to find a "pattern" string within a "text" string.

def compute_prefix_function(pattern):
    k = 0
    prefix = [0] * len(pattern)
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]
        if pattern[k + 1] == pattern[q]:
            k = k + 1
        prefix[q] = k
    return prefix

def KMP_search(text, pattern):
    prefix = compute_prefix_function(pattern)
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == len(pattern):
            return i - len(pattern) + 1
    return False

def main():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern: ")
    start_index = KMP_search(text, pattern)
    if start_index is not False:
        print(f"Pattern found at index {start_index}.")
    else:
        print("Pattern not found in the text.")

if __name__ == "__main__":
    main()