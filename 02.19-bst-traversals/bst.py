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
    # Return the result of finding the given key at the given bst's root.
    pass


def _find(node, key):
    # If the given node is None, then:
    #     (the given key does not exist)
    # Else if the given key is equal to the given node's key, then:
    #     (the given node contains the given key)
    # Else if the given key is less than the given node's key, then:
    #     Return the result of finding the given key at the given node's left.
    # Else, do:
    #     Return the result of finding the given key at the given node's right.
    pass


def insert(bst, key):
    # Set the given bst's root to the result of inserting the given key into
    #  the given bst's root.
    pass


def _insert(bst, node, key):
    # If the given node is None, then:
    #     Create a new node containing the given key.
    #     Increment the size.
    #     Return the new node.
    # Else if the given key is equal to the given node's key, then:
    #     (the given key is already in the given node -- do whatever is
    #      supposed to be done with duplicate keys, e.g., overwrite its value)
    #     Return the given node.
    # Else if the given key is less than the given node's key, then:
    #     Set the given node's left to the result of recursively inserting the
    #      given key into the given node's left.
    #     Return the given node.
    # Else, do:
    #     Set the given node's right to the result of recursively inserting the
    #      given key into the given node's right.
    #     Return the given node.
    pass


def remove(bst, key):
    # Set the given bst's root to the result of removing the given key from
    #  the given bst's root.
    pass


def _remove(bst, node, key):
    # If the given node is None, then:
    #     (the given key does not exist in the given BST -- do whatever is
    #      supposed to be done when removing nonexistent keys, e.g., raise an
    #      error)
    # Else if the given key is equal to the given node's key, then:
    #     If the given node's right is None, then:
    #         Decrement the size.
    #         Return the given node's left.
    #     Else if the given node's left is None, then:
    #         Decrement the size.
    #         Return the given node's right.
    #     Else, do:
    #         NOTE: Consider the smallest key in the right subtree:
    #                 * By definition, it is larger than any to the left.
    #                 * By construction, it is smaller than any to the right.
    #               ...thus, the smallest key to the right can *replace* the
    #               key in the given node and result in a valid BST.
    #
    #         Find the smallest key in the given node's right.
    #         Set the given node's right to the result of recursively removing
    #          that smallest key from the given node's right.
    #         Set the given node's key to that smallest key.
    #         Return the given node.
    #
    # Else if the given key is less than the given node's key, then:
    #     Set the given node's left to the result of recursively removing the
    #      given key from the given node's left.
    #     Return the given node.
    # Else, do:
    #     Set the given node's right to the result of recursively removing the
    #      given key from the given node's right.
    #     Return the given node.
    pass


def _min(node):
    # If the given node is None, then:
    #     (there is no smallest key)
    # Else if the given node's left is None, then:
    #     Return the given node's key.
    # Else, do:
    #     Return the result of recursing on the given node's left.
    pass


def inorder(bst):
    # Traverse the given bst's root.
    pass


def _traverse(node):
    # If the given node is None, then:
    #     (there is no node to traverse -- perform whatever default operation
    #      should be performed on empty trees)
    # Else, do:
    #     Recursively traverse the given node's left.
    #     (traverse the given node -- perform whatever operation should be
    #      performed on each node in the tree, e.g., enqueue it to a queue)
    #     Recursively traverse the given node's right.
    pass
