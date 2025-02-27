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
    # NOTE: This is essentially an array list in which the first step of any
    #       operation is to hash the given key, so as to convert the key (of
    #       any arbitrary type) into an integer (a valid array index).
    #
    # Hash the given key and mod it by the capacity.
    # Return the element at that hash code in the array.
    pass


def insert(dct, key, value):
    # TODO: This only works as long as there are no collisions. If ever two
    #       different keys were to hash to the same index, we would have no way
    #       of knowing which value was which.
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
