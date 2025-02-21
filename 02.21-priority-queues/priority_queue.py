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
    # TODO: Add the value as a node in the binary heap, which must be either
    #       the next leaf in the lowest (not-yet-filled) level or the first
    #       leaf in a new lowest (if the old lowest was filled) level, so as to
    #       maintain the completeness of the tree. Then rearrange the nodes in
    #       order to restore the heap property.
    pass


def dequeue(pqueue):
    # TODO: Remove the root node and replace it with the last leaf in the
    #       lowest level, so as to maintain the completeness of the tree. Then
    #       rearrange the nodes in order to restore the heap property.
    pass


def peek(pqueue):
    # NOTE: In a binary heap, the largest value -- the only value we actually
    #       care about in a priority queue -- must be at the root (the second
    #       largest must be one of the root's children, but there is no way of
    #       knowing which one; the smallest must be a leaf, but there is no way
    #       of knowing which one).
    #
    # (return the value at the root)
    pass
