import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()

        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    pass


def add_edge(graph, vertex_u, vertex_v):
    pass


def remove_vertex(graph, vertex):
    pass


def remove_edge(graph, vertex_u, vertex_v):
    pass


def path(graph, vertex_u, vertex_v):
    pass
