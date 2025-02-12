class BinarySearchTree:
    """ A binary search tree """

    def __init__(self):
        # The root of this tree:
        self.root = None
        # The number of nodes in this tree:
        self.size = 0


class Node:
    """ A single node in a binary search tree """

    def __init__(self, key, left, right):
        # The key contained in this node:
        self.key = key
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def find(bst, key):
    pass


def insert(bst, key):
    # NOTE: See below -- when we call _insert, we pass it the existing root of
    #       the BST (without the given key), and it then return the new root
    #       of that BST (with the given key). Note that not all insertions will
    #       necessarily create new nodes.
    #
    # Set the given bst's root to the result of inserting the given key at the
    #  given bst's root.
    pass


def _insert(bst, node, key):
    # NOTE: Functions ought to take as input problems and produce as output
    #       solutions. Here, the input is the root node of a subtree without
    #       the key (the problem), and the output is the root node of the
    #       resulting subtree with the key (the solution).
    #
    # If the given node is None, then:
    #     Create a new node containing the given key.
    #     Increment the size.
    #     Return the new node.
    # Else if the given key is less than the given node's key, then:
    #     Set the given node's left to the result of recursively inserting the
    #      given key into the given node's left.
    #     Return the given node.
    # Else if the given key is greater than the given node's key, then:
    #     Set the given node's right to the result of recursively inserting the
    #      given key into the given node's right.
    #     Return the given node.
    # Else, do:
    #     (the given key is already in the given node -- do whatever is
    #      supposed to be done with duplicate keys, e.g., overwrite its value)
    #     Return the given node.
    pass


def remove(bst, key):
    pass


def inorder(bst):
    pass
