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
    # Start with i being the size.
    # While i - 1 is greater than or equal to zero
    #  and the element at i - 1 is greater than the given value, do:
    #     Set the element at i in the array to the element at i - 1.
    #     Decrement i.
    #
    # Set the element at i in the array to the given value.
    # Increment the size.
    pass


def remove(lst, idx):
    # For i from the given idx to the size - 1, do:
    #     Set the element at i in the array to the element at i + 1.
    #
    # Decrement the size.
    pass


def find(lst, value):
    # Start with the low index being 0 and the high index being size - 1.
    #
    # While the low index is less than or equal to the high index, do:
    #     Set the mid index to (high + low) // 2.
    #     If the element at mid in the array is equal to the given value, then:
    #         Return mid.
    #     Else if the element at mid is less than the given value, then:
    #         Set the low index to mid + 1.
    #     Else, do:
    #         Set the high index to mid - 1.
    #
    # Return (the given value is not in the given list).
    pass


def create(array, size):
    # Sort the given array: low is 0, high is size - 1.
    # Return a new sorted list containing the sorted array.
    pass


def _sort(array, low, high):
    # NOTE: It is possible to write an iterative merge sort -- it is possible
    #       to write *anything* iteratively -- but a merge sort lends itself
    #       naturally to recursion. We must repeatedly identify and sort
    #       smaller arrays: smaller versions of the same problem.
    #
    # If low is equal to high:
    #     Return (a new array containing the element at low in the array).
    # Else, do:
    #     Set the mid index to (high + low) // 2.
    #     Recursively sort the left half: low is low, high is mid.
    #     Recursively sort the right half: low is mid + 1, high is high.
    #     Merge the sorted halves.
    #     Return the merged array.
    pass

def _merge(array_a, size_a, array_b, size_b):
    # Create a new array of capacity size_a + size_b.
    # Start with indices i, j, and k all being 0.
    #
    # While i is less than size_a or j is less than size_b, do:
    #     If i is greater than or equal to size_a, then:
    #         Set element k of the new array to element j of array_b.
    #         Increment j and k.
    #     Else if j is greater than or equal to size_b, then:
    #         Set element k of the new array to element i of array_a.
    #         Increment i and k.
    #     Else if element j of array_b is less than element i of array_a, then:
    #         Set element k of the new array to element j of array_b.
    #         Increment j and k.
    #     Else, do:
    #         Set element k of the new array to element i of array_a.
    #         Increment i and k.
    #
    # Return the new array.
    pass
