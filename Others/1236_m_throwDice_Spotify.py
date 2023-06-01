# Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.
# For example, throw_dice(3, 6, 7) should equal 15.

def throw_dice(N, faces, total):
    dp = [[0 for j in range(total + 1)]
        for i in range (N + 1)]
    
    for i in range(1, min(faces + 1, total + 1)):
        dp[1][i] = 1

    for i in range(2, N + 1):
        for j in range(1, total + 1):
            for k in range(1, min(faces + 1, j)):
                dp[i][j] += dp[i-1][j-k]
    
    return dp[N][total]

def main():
    N = int(input("Enter the number of dices: "))
    faces = int(input("Enter the number of faces in each dice: "))
    total = int(input("Enter the total required: "))
    print(throw_dice(N, faces, total))

if __name__ == "__main__":
    main()