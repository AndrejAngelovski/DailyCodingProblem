# Given a string, determine whether any permutation of it is a palindrome.
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

def can_form_palindrome(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    odd_counts_chars = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_counts_chars += 1
    
    if odd_counts_chars > 1:
        return False
    
    return True

def main():
    s1 = input("Enter a string: ")
    print(f'Can {s1} form a palindrome? {can_form_palindrome(s1)}')
    
if __name__ == "__main__":
    main()