class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0


def insert(lst, value):
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array)
    #     Set the array to the new array.
    #
    # NOTE: Inserting into a sorted list is almost exactly the same as adding
    #       to an array list; the fundamental difference is that we won't be
    #       given an index at which to insert. We have to find the appropriate
    #       index in order to maintain sorted order.
    #
    # Start with i being the size.
    # While i - 1 is greater than or equal to zero
    #  and the element at i - 1 is greater than the given value, do:
    #     Set the element at i in the array to the element at i - 1.
    #     Decrement i.
    #
    # Set the element at the given idx in the array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Likewise, removing from a sorted list is the same as removing from
    #       an array list while maintaining sorted order -- in the case of
    #       removing, that requires no additional logic, because removing from
    #       a sorted list cannot possibly result in an unsorted list.
    #
    # For i from the given idx to the size - 1, do:
    #     Set the element at i in the array to the element at i + 1.
    #
    # Decrement the size.
    pass


def find(lst, value):
    # Start with the low index being 0 and the high index being size - 1.
    #
    # While the low index is less than or equal to the high index, do:
    #    Set the mid index to (high + low) // 2.
    #    If the element at mid in the array is equal to the given value, then:
    #        Return mid.
    #    Else if the element at mid is less than the given value, then:
    #        Set the low index to mid + 1.
    #    Else, do:
    #        Set the high index to mid - 1.
    #
    # Return (the given value is not in the given list).
    pass


def create(array, size):
    # NOTE: This is not the best possible way to sort -- essentially, it turns
    #       out to be faster to consider sorting all elements at once instead
    #       of one element at a time -- but given a working insertion function,
    #       an insertion sort is trivial to implement.
    #
    # Create a new, empty sorted list.
    #
    # For i from 0 to the given size, do:
    #     Insert the element at i in the given array into the new sorted list.
    #
    # Return the new sorted list.
    pass
