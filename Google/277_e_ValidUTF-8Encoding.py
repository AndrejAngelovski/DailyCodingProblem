# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

# For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:

# For a single-byte character, the first bit must be zero.
# For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
# Visually, this can be represented as follows.

#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.

def is_valid_UTF8(data):
    count = 0
    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0

def main():
    data = list(map(int, input("Enter the array of integers (separated by space): ").split()))
    if is_valid_UTF8(data):
        print("It is a valid UTF-8 encoding.")
    else:
        print("It is not a valid UTF-8 encoding.")
    
if __name__ == "__main__":
    main()