# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def contstruct_tree(postorder):
    if not postorder:
        return None
    
    # The last eleement in the postorder sequence is the root
    root_val = postorder[-1]
    root = Node(root_val)

    # Partition the sequence into left and right subtrees
    partition = 0
    for i in range(len(postorder)-1):
        if postorder[i] < root_val:
            partition = i+1

    left = postorder[:partition]
    right = postorder[partition:-1]

   # Recursively construct the left and right subtrees
    root.left = contstruct_tree(left)
    root.right = contstruct_tree(right)

    return root

postorder = [2, 4, 3, 8, 7, 5]
root = contstruct_tree(postorder)

def print_preorder(node):
    if node:
        print(node.val),
        print_preorder(node.left)
        print_preorder(node.right)

print_preorder(root)