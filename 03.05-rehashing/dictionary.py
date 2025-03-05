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
    # Start with a current node being the head at that hash code.
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    #
    # Return the current node's value.
    pass


def insert(dct, key, value):
    # NOTE: Once the size is equal to the capacity -- once the load factor
    #       exceeds 1 -- a collision is inevitable, and the hash table must be
    #       rehashed in order to prevent the linked lists from getting too
    #       long. Ideally, the new capacity would be prime, but doubling and
    #       adding one is a decent compromise that is easy to compute.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2 + 1.
    #     Create a new array of that capacity.
    #
    #     NOTE: The hash codes were previously computed mod the old capacity.
    #           Now that the capacity has changed, all of the existing elements
    #           must be rehashed and potentially moved to new indices. The
    #           table is essentially a doubly nested list, where the outer list
    #           is an array list and the inner lists are linked lists. Further
    #           note that it is generally possible for two existing keys to
    #           collide after rehashing, however, all keys being rehashed must
    #           be unique, so colliding keys can be placed at the beginnings of
    #           their linked lists instead of the ends.
    #
    #     For i from 0 to the old capacity, do:
    #         Start with a current node being the head at index i.
    #         While the current node is not None, do:
    #             Rehash the current node's key and mod it by the new capacity.
    #             (insert the current node at the head at that new hash code in
    #              the new array)
    #             Set the current node to the current node's next.
    #
    #     Set the array to the new array.
    #
    # Hash the given key and mod it by the capacity.
    #
    # If the head at that hash code in the array is None, then:
    #     Create a new node containing the given key and value.
    #     Set the new node's next to None.
    #     Set the head at that hash code in the array to the new node.
    #     Increment the size.
    # Else, do:
    #     Start with a current node being the head at that hash code.
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None, then:
    #             Create a new node containing the given key and value.
    #             Set the new node's next to None.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
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
    # TODO: Iterate over all of the key-value pairs, just as in rehashing: loop
    #       through all indices in the array, then loop through all nodes in
    #       each corresponding linked list. Rather than rehashing those nodes,
    #       add their keys to a new list to be returned.
    pass
