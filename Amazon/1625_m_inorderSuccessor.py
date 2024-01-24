class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

def findMin(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorderSuccessor(node):
    if node is None:
        return None
    
    if node.right is not None:
        return findMin(node.right)
    
    p = node.parent
    while p is not None and node == p.right:
        node = p
        p = p.parent

    return p


if __name__ == "__main__":
    # Constructing the tree
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.left.parent = root
    root.right = TreeNode(22)
    root.right.parent = root
    root.left.left = TreeNode(4)
    root.left.left.parent = root.left
    root.left.right = TreeNode(12)
    root.left.right.parent = root.left
    root.left.right.left = TreeNode(10)
    root.left.right.left.parent = root.left.right
    root.left.right.right = TreeNode(14)
    root.left.right.right.parent = root.left.right

    
    node = root.left.right.right

    successor = inorderSuccessor(node)
    print(f"Inorder successor of {node.val} is:", end=" ")
    if successor:
        print(successor.val)
    else:
        print("No inorder successor")