import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    # Create a new empty dictionary (the vertex has no neighbors yet).
    # Insert the given vertex into the matrix, mapped to that dictionary.
    pass


def add_edge(graph, vertex_u, vertex_v):
    # Get vertex_u's dictionary from the matrix.
    # Insert vertex_v into vertex_u's dictionary, mapped to 1.
    # Get vertex_v's dictionary from the matrix.
    # Insert vertex_u into vertex_v's dictionary, mapped to 1.
    # Increment the size.
    pass


def remove_vertex(graph, vertex):
    # Get the given vertex's dictionary from the matrix.
    # Get the list of that dictionary's keys (the given vertex's neighbors).
    #
    # For i from 0 to that list's size, do:
    #     Get the i'th element of that list (the given vertex's i'th neighbor).
    #     Remove the edge between the given vertex and the i'th element.
    #
    # Remove the given vertex from the matrix.
    pass


def remove_edge(graph, vertex_u, vertex_v):
    # Get vertex_u's dictionary from the matrix.
    # Remove vertex_v from vertex_u's dictionary.
    # Get vertex_v's dictionary from the matrix.
    # Remove vertex_u from vertex_v's dictionary.
    # Decrement the size.
    pass


def path(graph, vertex_u, vertex_v):
    pass
