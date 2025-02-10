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
    # Create a new tree containing the given value.
    # Set the new tree's root's left to the given left tree's root.
    # Set the new tree's root's right to the given right tree's root.
    # Set the new tree's size to the sum of the given left tree's size, the
    #  given right tree's size, and 1 (for the new root).
    # Return the new tree.
    pass


def postorder(tree):
    # Traverse the given tree's root.
    pass


def _traverse(node):
    # If the given node is None, then:
    #     (there is no node to traverse -- perform whatever default operation
    #      should be performed on empty trees)
    # Else, do:
    #     Recursively traverse the given node's left.
    #     Recursively traverse the given node's right.
    #     (traverse the given node -- perform whatever operation should be
    #      performed on each node in the tree, e.g., enqueue it to a queue)
    pass


def preorder(tree):
    pass


def levelorder(tree):
    pass
