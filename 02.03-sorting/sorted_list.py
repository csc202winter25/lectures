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
    #       to an unsorted array list. The fundamental difference is that the
    #       caller cannot specify an index at which to insert; we have to find
    #       the appropriate index to maintain sorted order.
    #
    # Start with i being the size.
    # While i - 1 is greater than or equal to 0
    #  and the element at i - 1 is greater than the given value do:
    #     Set the element at i in the array to the element at i - 1.
    #     Decrement i.
    #
    # Set the element at i in the array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # NOTE: Similarly, removing from a sorted list ought to be the same as
    #       removing from an unsorted list, we just have to maintain sorted
    #       order -- which, in the case of remove, requires *no* additional
    #       logic, because we cannot ruin sorted order by *removing* elements.
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
    # NOTE: This is not the most efficient way to sort a list -- it has worst-
    #       and average-case complexity O(n^2) -- but it is trivial to
    #       implement given a working "insert" function.
    #
    # Create a new, empty sorted list.
    # For i from 0 to the given size - 1, do:
    #     Insert the element at i in the given array into the new sorted list.
    # Return the new sorted list.
    pass
