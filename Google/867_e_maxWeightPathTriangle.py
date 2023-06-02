# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
# Write a program that returns the weight of the maximum weight path.

def max_weight_path(triangle):
    if not triangle:
        return 0
    
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]

def main():
    triangle = []
    n = int(input("Enter the number of rows in the triangle: "))
    for i in range(n):
        row = list(map(int, input(f"Enter the elements of row {i + 1} separated by space: ").split()))
        triangle.append(row)
    print("Maximum weight of the path is: ", max_weight_path(triangle))

if __name__ == "__main__":
    main()