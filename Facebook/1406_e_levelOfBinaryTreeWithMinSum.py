# Given a binary tree, return the level of the tree with minimum sum.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def min_sum_level(root):
    if not root:
        return -1
    
    level = 0
    min_sum_level = 0
    min_sum = float('inf')

    queue = [(root, 0)]

    while queue:
        level_sum = sum(node.value for node, node_level in queue if node_level == level)
        if level_sum < min_sum:
            min_sum = level_sum
            min_sum_level = level

        queue = [(node.left, level + 1) for node, node_level in queue if node.left] + \
        [(node.right, level + 1) for node, node_level in queue if node.right]
        level += 1
    return min_sum_level

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Level with minimum sum is:", min_sum_level(root))

if __name__ == "__main__":
    main()