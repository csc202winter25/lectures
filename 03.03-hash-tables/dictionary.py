class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    #
    # Start with the current node being the head at that hash code.
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    #
    # Return the given node's value.
    pass


def insert(dct, key, value):
    # Hash the given key and mod it by the capacity.
    #
    # If the head at that hash code in the array is None, then:
    #     Create a new node containing the given key and value.
    #     Set the new node's next to None.
    #     Set the head at that hash code in the array to the new node.
    #     Increment the size.
    # Else, do:
    #     NOTE: Essentially, a separate chaining hash table stores key-value
    #           pairs in a bunch of (hopefully) smaller linked lists, then uses
    #           a hash function quickly narrow down which list might contain
    #           the key-value pair we are interested in.
    #
    #     Start with the current node being the head at that hash code.
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None, then:
    #             Create a new node containing the given key and value.
    #             Set the new node's next to None.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
    #
    #     NOTE: The only way to break out of the loop is to have a current node
    #           whose key is the given key -- whether because that node already
    #           existed in the hash table, or because it was just created and
    #           added to the hash table.
    #
    #     Set the current node's value to the given value.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    #
    # If the head at that hash code contains the given key, then:
    #     Set the head at that hash code to its next.
    # Else, do:
    #     Start with a current node being the head at that hash code.
    #     While the current node's next's key is not the given key, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    #
    # Decrement the size.
    pass


def keys(dct):
    pass
