# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.
# For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

# B B W
# W W W
# W W W
# B B B
# Becomes

# B B G
# G G G
# G G G
# B B B

def flood_fill(image, sr, sc, newColor):
    rows, cols, oldColor = len(image), len(image[0]), image[sr][sc]

    # Base case for recursion
    if oldColor == newColor:
        return image

    def dfs(r, c):
        # If the node is out of bounds or is not from the old color
        # then it is not eligible for color change.
        if (not (0 <= r < rows and 0 <= c < cols)) or image[r][c] != oldColor:
            return
    
        # Recur for all surrounding cells
        image[r][c] = newColor
        [dfs(r + x, c + y) for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0))]

    dfs(sr, sc)
    return image

def main():
    image = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B'],
    ]
    sr, sc, newColor = 2, 2, 'G'
    updated_image = flood_fill(image, sr, sc, newColor)

    for row in updated_image:
        print(' '.join(row))

if __name__ == "__main__":
    main()