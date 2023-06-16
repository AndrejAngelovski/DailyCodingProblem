# Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.

def find_min_difference(arr):
    total_sum = sum(arr)
    n = len(arr)
    dp = [[0 for _ in range(total_sum + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]
    diff = float('inf')
    for i in range(total_sum // 2, -1, -1):
        if dp[n][i]:
            diff = total_sum - (2 * i)
            break
    return diff


def main():
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    print("The minimum difference is: ", find_min_difference(arr))


if __name__ == "__main__":
    main()
