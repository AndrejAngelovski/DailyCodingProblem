class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def find_second_largest(root):
    if root is None:
        return None
    
    current = root
    # Traverse to the rightmost node (largest node)
    while current.right is not None:
        current = current.right

    if current.left is not None:
        current = current.left
        while current.right is not None:
            current = current.right
        return current.value
    
    else:
        while current.parent is not None and current.parent.right is not current:
            current = current.parent
        return current.parent.value if current.parent is not None else None
    
nodes = [TreeNode(i) for i in [20, 10, 30, 15, 25, 40, 27, 50]]

nodes[0].left, nodes[0].right = nodes[1], nodes[2]
nodes[1].parent, nodes[2].parent = nodes[0], nodes[0]
nodes[1].right = nodes[3]
nodes[3].parent = nodes[1]
nodes[2].left, nodes[2].right = nodes[4], nodes[5]
nodes[4].parent, nodes[5].parent = nodes[2], nodes[2]
nodes[4].right = nodes[6]
nodes[6].parent = nodes[4]
nodes[5].right = nodes[7]
nodes[7].parent = nodes[5]

second_largest_value = find_second_largest(nodes[0])
print(second_largest_value)