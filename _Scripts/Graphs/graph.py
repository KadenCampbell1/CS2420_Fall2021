"""
Project 7: Graphs
Author: Kaden Campbell
Course: CS2420
Date: 12/2/2021

The graph class creates a graph object.

__init__ arguments:
None

Functions:
set_head(node) -- sets head to node
get_head(): -- returns self.head
"""

import math


class Graph:
    def __init__(self):
        pass

    def add_vertex(self, label):
        """adds a vertex with the specified label.

        Returns the graph. Label must be a string or a ValueError occurs
        """
        pass

    def add_edge(self, src, dest, w):
        """adds an edge from vertex src to vertex dest with weight w.

        Returns the graph. ValueError if occurs when src, dest, and w are not valid.
        """
        pass

    def get_weight(self, src, dest):
        """Returns the weight on edge src-dest.

         Returns math.inf if no path exists. ValueError occurs if src or dest is not in the graph.
         """
        pass

    def dfs(self, starting_vertex):
        """Returns generator from traversing the graph in depth-first order.

        Starts from the specified vertex and raises a ValueError if the vertex does not exist.
        """
        pass

    def bfs(self, starting_vertex):
        """Returns a generator for traversing the graph in breadth-first order.

        Starts from the specified vertex and raises a ValueError if the vertex does not exist.
        """
        pass

    def dsp(self, src, dest):
        """Returns a tuple of path length and list of path from dest to src.

        If no path exists, returns the tuple (math.inf, empty list.)
        """
        pass

    def dsp_all(self, src):
        """Returns a dictionary of the shortest weighted path between src and all other vertices.

         Implements Dijkstra's Shortest Path algorithm. The key is the the destination vertex label,
         the value is a list of vertices on the path from src to dest.
         """
        pass

    def __str__(self):
        """returns string of Graph using GraphViz"""
        """https://graphs.grevian.org/example"""
        pass


def main():
    """Tests Graph ADT"""
    pass


if __name__ == "__main__":
    main()
