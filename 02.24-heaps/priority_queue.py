class PriorityQueue:
    """ A prioritized collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0


def enqueue(pqueue, value):
    # TODO: Adding the value as a new node in the tree, either the next leaf in
    #       the lowest (partially filled) level or the first leaf in a new
    #       lowest (if the lowest was full) level, maintains the completeness
    #       of the tree. Then repeatedly swap the current node with its parent
    #       if the current node is larger, to restore the heap property.
    #
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity + 1.
    #     (copy the elements from the old array into the new array)
    #     Set the array to the new array.
    #
    # Start with index i being the index of the next leaf (index size + 1).
    # Set element i to the given value.
    #
    # While i is greater than 1 (i is not the root), do:
    #     If element i is greater than element i // 2, then:
    #         Swap element i with element i // 2.
    #         Set i to i // 2.
    #     Else, do:
    #         (all elements are already in the right place)
    #
    # Increment the size.
    pass


def dequeue(pqueue):
    # NOTE: Removing the root and replacing it with the last leaf in the lowest
    #       level (the same very particular position to which we add leaves
    #       when enqueueing) maintains both the structural integrity and the
    #       completeness of the tree. Then repeatedly swap the current node
    #       with its larger child if the current node is smaller.
    #
    # Start with index i being the index of the root (index 1).
    # Set element i to the value of the last leaf (index size).
    #
    # While 2 * i is less than or equal to size (i is not a leaf), do:
    #     If 2 * i + 1 is greater than size or element 2 * i is greater than
    #      element 2 * i + 1, then:
    #         If element 2 * i is greater than element i, then:
    #             Swap element i with element 2 * i.
    #             Set i to 2 * i.
    #         Else, do:
    #             (all elements are already in the right place)
    #     Else, do:
    #         If element 2 * i + 1 is greater than element i, then:
    #             Swap element i with element 2 * i + 1.
    #             Set i to 2 * i + 1.
    #         Else, do:
    #             (all elements are already in the right place)
    #
    # Decrement the size.
    pass


def peek(pqueue):
    # NOTE: In a binary heap, the largest value -- the only value we actually
    #       care about in a priority queue -- must be at the root (the second
    #       largest must be one of the root's children, but there is no way of
    #       knowing which one; the smallest must be a leaf, but there is no way
    #       of knowing which one).
    #
    # Return element 1.
    pass
