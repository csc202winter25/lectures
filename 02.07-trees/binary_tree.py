class BinaryTree:
    """ A binary tree """

    def __init__(self, value = None):
        if value is None:
            # The root of this empty tree:
            self.root = None
            # The number of nodes in this tree:
            self.size = 0
        else:
            # The root of this singleton tree:
            self.root = Node(value, None, None)
            # The number of nodes in this tree:
            self.size = 1


class Node:
    """ A single node in a binary tree """

    def __init__(self, value, left, right):
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def combine(value, left, right):
    pass


def postorder(tree):
    pass


def preorder(tree):
    pass


def levelorder(tree):
    pass
