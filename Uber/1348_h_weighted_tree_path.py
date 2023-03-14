# Given a tree where each edge has a weight, compute the length of the longest path in the tree.

# For example, given the following tree:

#    a
#   /|\
#  b c d
#     / \
#    e   f
#   / \
#  g   h
# and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

# The path does not have to pass through the root, and each node can have any amount of children.

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.weight = 0


def dfs(node, path_len):
    if not node.children:
        return path_len
    max_child_len = 0
    for child in node.children:
        child_len = dfs(child, child.weight)
        max_child_len = max(max_child_len, child_len)
    max_len = max(max_child_len, path_len)
    return max_len


def longest_path(root):
    max_length = 0
    for child in root.children:
        length = dfs(child, 0)
        max_length = max(max_length, length)
    return max_length


# Example usage
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.children = [b, c, d]
d.children = [e, f]
e.children = [g, h]

# Setting weights
a_b, a_c, a_d, d_e, d_f, e_g, e_h = 3, 5, 8, 2, 4, 1, 1
b.weight = a_b
c.weight = a_c
d.weight = a_d
e.weight = d_e
f.weight = d_f
g.weight = e_g
h.weight = e_h

print(longest_path(a))
