# Given an integer N, construct all possible binary search trees with N nodes.
from tqdm import tqdm

class Node:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

def construct_trees(start, end):
    trees = []

    if start > end:
        trees.append(None)
        return trees

    # wrap the outermost loop with tqdm
    for i in tqdm(range(start, end+1)):
        left_subtree = construct_trees(start, i-1)
        right_subtree = construct_trees(i+1, end)

        for j in range(len(left_subtree)):
            left = left_subtree[j]
            for k in range(len(right_subtree)):
                right = right_subtree[k]
                node = Node(i) # make i as root
                node.left = left
                node.right = right
                trees.append(node)
    return trees

def main():
    n = int(input("Enter the number of nodes: "))
    trees = construct_trees(1, n)
    print(f"Total number of Binary Search Trees with {n} nodes is {len(trees)}")

if __name__ == "__main__":
    main()
