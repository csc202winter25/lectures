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
    # Set the bst's root to the result of inserting the key at that root.
    pass


def _insert(bst, node, key):
    # NOTE: Functions ought to take as input problems and produce as output
    #       solutions. In this case, the input is a tree without the given key
    #       (the problem) and the solution ought to be the tree with that given
    #       key (the solution).
    #
    # If the given node is None, then:
    #     Create a new node containing the given key with no children.
    #     Increment the given bst's size.
    #     Return the new node.
    # Else if the given key is equal to the given node's key:
    #     (the key is already in the BST -- do whatever is supposed to be done
    #      with duplicate keys, e.g., overwrite their associated value)
    #     Return the given node.
    # Else if the given key is less than the given node's key:
    #     Set the given node's left to the result of inserting the given key at
    #      the given node's left.
    #     Return the given node.
    # Else if the given key is greater than the given node's key:
    #     Set the given node's right to the result of inserting the given key
    #      at the given node's right.
    #     Return the given node.
    pass


def remove(bst, key):
    pass


def inorder(bst):
    pass
