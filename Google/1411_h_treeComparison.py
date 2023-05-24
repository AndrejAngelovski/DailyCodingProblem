class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def isSubtree(s, t):
    if s is None:
        return False
    if isSame(s, t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def isSame(s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)