from Vertex import Vertex

"""
Graph Class
----------

This class represents the Graph modelling our courier network. 

Each Graph consists of the following properties:
    - vertices: A list of vertices comprising the graph

The class also supports the following functions:
    - add_vertex(vertex): Adds the vertex to the graph
    - remove_vertex(vertex): Removes the vertex from the graph
    - add_edge(vertex_A, vertex_B): Adds an edge between the two vertices
    - remove_edge(vertex_A, vertex_B): Removes an edge between the two vertices
    - send_message(s, t): Returns a valid path from s to t containing at most one untrusted vertex
    - check_security(s, t): Returns the set of edges that, if any are removed, would result in any s-t path having to use an untrusted edge

Your task is to complete the following functions which are marked by the TODO comment.
Note that your modifications to the structure of the Graph should be correctly updated in the underlying Vertex class!
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Graph():
    # These are the defined properties as described above
    vertices: 'list[Vertex]'

    def __init__(self) -> None:
        """
        The constructor for the Graph class.
        """
        self.vertices = []

    def add_vertex(self, vertex: Vertex) -> None:
        """
        Adds the given vertex to the graph.
        If the vertex is already in the graph or is invalid, do nothing.
        :param vertex: The vertex to add to the graph.
        """

        # TODO Fill this in

    def remove_vertex(self, vertex: Vertex) -> None:
        """
        Removes the given vertex from the graph.
        If the vertex is not in the graph or is invalid, do nothing.
        :param vertex: The vertex to remove from the graph.
        """

        # TODO Fill this in

    def add_edge(self, vertex_A: Vertex, vertex_B: Vertex) -> None:
        """
        Adds an edge between the two vertices.
        If adding the edge would result in the graph no longer being simple or the vertices are invalid, do nothing.
        :param vertex_A: The first vertex.
        :param vertex_B: The second vertex.
        """

        # TODO Fill this in

    def remove_edge(self, vertex_A: Vertex, vertex_B: Vertex) -> None:
        """
        Removes an edge between the two vertices.
        If an existing edge does not exist or the vertices are invalid, do nothing.
        :param vertex_A: The first vertex.
        :param vertex_B: The second vertex.
        """

        # TODO Fill this in

    def send_message(self, s: Vertex, t: Vertex) -> 'list[Vertex]':
        """
        Returns a valid path from s to t containing at most one untrusted vertex.
        Any such path between s and t satisfying the above condition is acceptable.
        Both s and t can be assumed to be unique and trusted vertices.
        If no such path exists, return None.
        :param s: The starting vertex.
        :param t: The ending vertex.
        :return: A valid path from s to t containing at most one untrusted vertex.
        """

        # TODO Fill this in

    def check_security(self, s: Vertex, t: Vertex) -> 'list[(Vertex, Vertex)]':
        """
        Returns the list of edges as tuples of vertices (v1, v2) such that the removal 
        of the edge (v1, v2) means a path between s and t is not possible or must use
        two or more untrusted vertices in a row. v1 and v2 must also satisfy the criteria
        that exactly one of v1 or v2 is trusted and the other untrusted.        
        Both s and t can be assumed to be unique and trusted vertices.
        :param s: The starting vertex
        :param t: The ending vertex
        :return: A list of edges which, if removed, means a path from s to t uses an untrusted edge or is no longer possible. 
        Note these edges can be returned in any order and are unordered.
        """

        # TODO Fill this in
