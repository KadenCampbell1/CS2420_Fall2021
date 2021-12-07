"""
Project 7: Graphs
Author: Kaden Campbell
Course: CS2420
Date: 12/2/2021

The graph class creates a graph object.

__init__ arguments:
None

Functions:
add_vertex(label) -- adds a vertex with the specified label
add_edge(src, dest, w) -- adds an edge from vertex src to vertex dest with weight w
get_weight(src, dest) -- Returns the weight on edge src-dest
build_matrix() -- Returns a matrix representation of the graph
dfs(starting_vertex) -- Returns generator from traversing the graph in depth-first order
bfs(starting_vertex) -- Returns a generator for traversing the graph in breadth-first order
dsp(src, dest) -- Returns a tuple of path length and list of path from dest to src
dsp_all(src) -- Returns a dictionary of the shortest weighted path between src and all other vertices
__str__() -- returns string of Graph using GraphViz
"""

import math
import graphviz


class Graph:
    def __init__(self):
        self.info_graph = {}
        self.edge_graph = {}

    def add_vertex(self, label):
        """adds a vertex with the specified label.

        Returns the graph. Label must be a string or a ValueError occurs
        """

        if not isinstance(label, str):
            raise ValueError

        self.info_graph[label] = None
        return self

    def add_edge(self, src, dest, w):
        """adds an edge from vertex src to vertex dest with weight w.

        Returns the graph. ValueError if occurs when src, dest, and w are not valid.
        """
        if not isinstance(src, str):
            raise ValueError
        if not isinstance(dest, str):
            raise ValueError
        if not isinstance(w, float):
            raise ValueError
        keys = self.info_graph.keys()
        if src not in keys:
            raise ValueError("src not in graph")
        if dest not in keys:
            raise ValueError("dest not in graph")

        if src not in self.edge_graph.keys():
            self.edge_graph[src] = [(dest, w)]
        else:
            other_values = self.edge_graph[src]
            temp = []
            for i in other_values:
                temp.append(i)
            temp.append((dest, w))
            self.edge_graph[src] = temp
        return self

    def get_weight(self, src, dest):
        """Returns the weight on edge src-dest.

         Returns math.inf if no path exists. ValueError occurs if src or dest is not in the graph.
         """
        keys = self.info_graph.keys()
        if src not in keys:
            raise ValueError("src not in graph")
        if dest not in keys:
            raise ValueError("dest not in graph")

        if src == dest:
            return 0

        if src in self.edge_graph.keys():
            for i in self.edge_graph[src]:
                if i[0] == dest:
                    return i[1]

        return math.inf

    def build_matrix(self):
        """builds and returns a matrix representation of the graph"""
        m_graph = []
        temp_lyst = []
        for i in self.info_graph.keys():
            temp_lyst.append(i)

        m_graph.append(temp_lyst)
        temp_lyst = []
        lyst_end = 0
        while lyst_end < len(m_graph[0]):
            source = m_graph[0][lyst_end]
            for j in m_graph[0]:
                temp_lyst.append(self.get_weight(source, j))
            m_graph.append(temp_lyst)
            temp_lyst = []
            lyst_end += 1
        return m_graph

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
        """returns string of Graph using GraphViz notation"""
        """https://graphs.grevian.org/example"""

        graph_str = "digraph G {\n"
        for i in self.edge_graph.keys():
            for j in self.edge_graph[i]:
                graph_str += f'   {i} -> {j[0]} [label="1.0",weight="{j[1]}"];\n'
        graph_str += "}\n"
        return graph_str


def test_vertex_edge_weight():
    g = Graph()
    try:
        g.add_vertex(0)
    except ValueError:
        print("1ValueError True")
    g.add_vertex("A")
    x = g.add_vertex("B")
    try:
        g.add_edge("A", "cat", 10.0)

    except ValueError:
        print("2ValueError True")
    try:
        g.add_edge("A", "B", "cat")

    except ValueError:
        print("3ValueError True")
    if isinstance(x, Graph):
        print("4instance True")
    x = g.add_edge("A", "B", 10.0)
    if g.get_weight("A", "B") == 10:
        print("5is 10")
    if g.get_weight("B", "A") == math.inf:
        print("6is inf")
    if isinstance(x, Graph):
        print("7is instance")


def test_print():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)


    expected ='''digraph G {
   A -> B [label="1.0",weight="1.0"];
   A -> C [label="1.0",weight="1.0"];
   B -> D [label="1.0",weight="1.0"];
   C -> E [label="1.0",weight="1.0"];
   E -> F [label="1.0",weight="1.0"];
}
'''
    output = str(g)
    if output == expected:
        print("True")
    else:
        print("False")


def test_bfs():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 1.0)
    g.add_edge("A", "C", 1.0)

    g.add_edge("B", "D", 1.0)

    g.add_edge("C", "E", 1.0)

    g.add_edge("E", "F", 1.0)

    gen = g.bfs("A")
    data = [x for x in gen]
    if data[0] == "A":
        print("data is A")
    if data[-1] == "F":
        print("data is F")
    if len(data) == 6:
        print("len is 6")
    gen = g.bfs("C")
    data = [x for x in gen]
    if len(data) == 3:
        print("data is 3")


def main():
    """Tests Graph ADT"""
    # g = Graph()
    # g.add_vertex("A")
    # g.add_vertex("B")
    # g.add_edge("A", "B", 10.0)
    # print(g.get_weight("A", "B"))
    # g.add_vertex("C")
    # g.add_edge("A", "C", 10.0)
    # print(g.get_weight("A", "B"))
    # g.add_vertex("D")
    #
    # print(g.build_matrix())

    # test_vertex_edge_weight()
    # test_print()
    test_bfs()


if __name__ == "__main__":
    main()
