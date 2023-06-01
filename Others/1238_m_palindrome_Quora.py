# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".

# Create a table of size n*n. dp[i][j] will store
# min number of insertions needed to convert s[i..j]
# to a palindrome.

def find_min_insertions(s):
    n = len(s)

    dp = [[0 for i in range(n)] for i in range(n)]

    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
            i += 1

    return dp[0][n-1]

def main():
    s = input("Enter a string: ")
    print(find_min_insertions(s))

if __name__ == "__main__":
    main()