class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


def get(dct, key):
    # NOTE: Essentially, this is an array list in which we have to convert the
    #       keys (of arbitrary type) into indices before we can access their
    #       values within the array.
    #
    # Hash the given key and mod it by the capacity.
    # Return the element at that hash code in the array.
    pass


def insert(dct, key, value):
    # TODO: This only works as long as there are no collisions. If two keys
    #       were ever to hash to the same index, we would have no way of
    #       knowing whether we were overwriting a different existing key.
    #
    # Hash the given key and mod it by the capacity.
    #
    # If the element at that hash code in the array is None, then:
    #     Set the element at that hash code in the array to the given value.
    #     Increment the size.
    # Else, do:
    #     Set the element at that hash code in the array to the given value.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    # Set the element at that hash code in the array to None.
    # Decrement the size.
    pass


def keys(dct):
    pass
