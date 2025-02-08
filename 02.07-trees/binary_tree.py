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
    # Set the new tree's root's left to the left tree's root.
    # Set the new tree's root's right to the right tree's root.
    # Set the new tree's size to the sum of the left tree's size, the right
    #  tree's size, and 1 (for the root).
    # Return the new tree.
    pass


def postorder(tree):
    # NOTE: Trees are recursively defined structures:
    #         * The smallest trees consist of 0 or 1 nodes.
    #         * All larger trees are the result of combining smaller trees.
    #       ...however, BinaryTree is *not* recursively defined; Node is. A
    #       BinaryTree does not contain BinaryTrees, but a Node contains Nodes.
    #
    # Traverse the given tree's root.
    pass


def _traverse(node):
    # NOTE: In a post-order traversal, parents are traversed after children,
    #       thus, we must recurse on our children before traversing ourselves.
    #
    # If the given node is None, then:
    #     (there is no node to traverse -- perform whatever default operation
    #      should be performed on empty trees)
    # Else, do:
    #     Recursively traverse the given node's left child.
    #     Recursively traverse the given node's right child.
    #     (traverse the given node -- perform whatever operation should be
    #      performed on each node in the tree, e.g., enqueue it to a queue)
    pass


def preorder(tree):
    pass


def levelorder(tree):
    pass
