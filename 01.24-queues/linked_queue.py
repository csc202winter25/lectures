class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this queue:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def enqueue(queue, value):
    # NOTE: Given both a reference to the head and a reference to the tail, it
    #       is possible to add to both the head or the tail in O(1) time. For
    #       the purposes of enqueueing, it arguably doesn't matter which
    #       terminus of the list is the front or back of the queue...
    #
    # Create a new node containing the given value.
    #
    # If the given queue's size is 0, then:
    #     Set the given queue's head to the new node.
    # Else, do:
    #     Set the given queue's tail's next to the new node.
    #
    # Set the given queue's tail to the new node.
    # Set the new node's next to None.
    # Increment the given lst's size.
    pass


def dequeue(queue):
    # NOTE: ...but removing from the head of a linked list is O(1), whereas
    #       removing from the tail is O(n), because we would have to traverse
    #       the entire list to find the second-to-last node. We would like the
    #       head of the list to be the front of the queue, thus, the tail must
    #       be the back.
    #
    # If the given queue's size is 1, then:
    #     Set the given queue's head and tail to None.
    # Else, do:
    #     Set the given queue's head to the given queue's head's next.
    #
    # Decrement the given queue's size.
    pass


def peek(queue):
    # Return the given queue's head's value.
    pass