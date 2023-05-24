class Node:
    def __init__(self, value=0):
        self.value = value
        self._left = None
        self._right = None

    @property
    def left(self):
        if self._left is None:
            self._left = Node(self.value + 1)
        return self._left

    @property
    def right(self):
        if self._right is None:
            self._right = Node(self.value + 1)
        return self._right


def generate():
    return Node()
