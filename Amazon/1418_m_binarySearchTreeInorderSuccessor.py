# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

# For example, the inorder successor of 22 is 30.

#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.

class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder_successor(node):
    if node.right is not None:
        return find_min(node.right)
    p = node.parent
    while p is not None:
        if node != p.right:
            break
        node = p
        p = p.parent
    return p
