# Implement regular expression matching with the following special characters:
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
# For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
# Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

def is_match(text, pattern):
    if not pattern:
        return not text
    
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (is_match(text, pattern[2:]) or
                first_match and is_match(text[1:], pattern))
    else:
        return first_match and is_match(text[1:], pattern[1:])
    
def main():
    s = input('Enter string: ')
    p = input('Enter pattern: ')
    print(is_match(s, p))

if __name__ == "__main__":
    main()