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
bfs_helper(starting_vertex) -- Builds a list for bfs() to use in breadth-first order traversal.
dfs_helper(starting_vertex) -- Builds a list for dfs() to use in depth-first order traversal.
dsp(src, dest) -- Returns a tuple of path length and list of path from dest to src
dsp_all(src) -- Returns a dictionary of the shortest weighted path between src and all other vertices
__str__() -- returns string of Graph using GraphViz
"""

import math


class Graph:
    def __init__(self):
        self.info_graph = {}
        self.edge_graph = {}
        self.all_paths = {}
        self.bfs_list = [None]
        self.dfs_list = [None]

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
        if not isinstance(w, float) and not isinstance(w, int):
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
        if starting_vertex not in self.info_graph.keys():
            raise ValueError("starting_vertex not in matrix")

        self.dfs_list = [starting_vertex]
        matrix = self.build_matrix()
        self.dfs_helper(starting_vertex, matrix)

        end = len(self.dfs_list)
        current = 0
        while current < end:
            yield self.dfs_list[current]
            current += 1

    def dfs_helper(self, starting_vertex, matrix):
        """Builds a list for dfs() to use in depth-first order traversal.

        Starts from the specified vertex and raises a ValueError if the vertex does not exist.
        """

        if starting_vertex not in self.dfs_list:
            self.dfs_list.append(starting_vertex)

        node = starting_vertex
        row = None
        for i, j in enumerate(matrix[0]):
            if j == node:
                row = i + 1
                break

        if row is not None:
            for k, l in enumerate(matrix[row]):
                if l != math.inf and l != 0:
                    if matrix[0][k] not in self.dfs_list:
                        self.dfs_helper(matrix[0][k], matrix)
        else:
            return

    def bfs(self, starting_vertex):
        """Returns a generator for traversing the graph in breadth-first order.

        Starts from the specified vertex and raises a ValueError if the vertex does not exist.
        """
        if starting_vertex not in self.info_graph.keys():
            raise ValueError("starting_vertex not in matrix")

        self.bfs_helper(starting_vertex)

        end = len(self.bfs_list)
        current = 0
        while current < end:
            yield self.bfs_list[current]
            current += 1

    def bfs_helper(self, starting_vertex):
        """Builds a list for bfs() to use in breadth-first order traversal.

        Starts from the specified vertex and raises a ValueError if the vertex does not exist.
        """

        matrix = self.build_matrix()
        self.bfs_list = [starting_vertex]
        visited_nodes = []
        current_node = starting_vertex

        visited_index = -1
        while visited_index < len(visited_nodes):
            visited_index += 1

            vertex_index = None
            for i, j in enumerate(matrix[0]):
                if j == current_node:
                    vertex_index = i + 1
                    break

            if vertex_index is not None:
                for k, value in enumerate(matrix[vertex_index]):
                    if value != math.inf and value != 0:
                        if matrix[0][k] not in visited_nodes:
                            visited_nodes.append(matrix[0][k])

            if visited_index < len(visited_nodes):
                current_node = visited_nodes[visited_index]

        for letter in visited_nodes:
            self.bfs_list.append(letter)

    def dsp(self, src, dest):
        """Returns a tuple of path length and list of path from dest to src.

        If no path exists, returns the tuple (math.inf, empty list.)
        """
        matrix = self.build_matrix()
        paths = ()
        visited_nodes = []
        temp_paths = {}
        current_weight = 0
        current_node = src

        for nodes in matrix[0]:
            temp_paths[nodes] = (math.inf, [])

        while current_node != dest:
            visited_nodes.append(current_node)
            row = None
            for i, j in enumerate(matrix[0]):
                if j == current_node:
                    row = i + 1
                    break

            if row is not None:
                for k, value in enumerate(matrix[row]):
                    if value != math.inf and value != 0:
                        temp_weight = value + current_weight
                        if temp_weight < temp_paths[matrix[0][k]][0]:
                            if len(temp_paths[matrix[0][k]][-1]) <= 0:
                                path_nodes = list(visited_nodes)
                                path_nodes.append(matrix[0][k])
                            else:
                                path_nodes = list(temp_paths[matrix[0][k]][-1])
                            temp_paths[matrix[0][k]] = (value + current_weight, path_nodes)

                temp_weight = math.inf
                for key in temp_paths.keys():
                    weight = temp_paths[key][0]
                    if weight < temp_weight and key not in visited_nodes:
                        temp_weight = weight
                        next_node = key
                current_node = next_node
                # set up second list like visited_nodes that resets here
                current_weight = temp_weight

        paths = temp_paths[dest]

        return paths

    def dsp_all(self, src):
        """Returns a dictionary of the shortest weighted path between src and all other vertices.

         Implements Dijkstra's Shortest Path algorithm. The key is the the destination vertex label,
         the value is a list of vertices on the path from src to dest.
         """
        matrix = self.build_matrix()
        self.all_paths = {}

        for i in matrix[0]:
            if i != src:
                self.all_paths[i] = self.dsp(src, i)

        return self.all_paths

    def __str__(self):
        """returns string of Graph using GraphViz notation"""
        """https://graphs.grevian.org/example"""

        graph_str = "digraph G {\n"
        for i in self.edge_graph.keys():
            for j in self.edge_graph[i]:
                graph_str += f'   {i} -> {j[0]} [label="{j[1]:.1f}",weight="{j[1]:.1f}"];\n'
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


def test_dfs():
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

    gen = g.dfs("A")
    data = [x for x in gen]
    if data[0] == "A":
        print("Data is A")
    if data[-1] in ("D", "F"):
        print("Data is in (D, F)")
    if len(data) == 6:
        print("data is len 6")
    gen = g.dfs("C")
    data = [x for x in gen]
    if len(data) == 3:
        print("data is len 3")


def test_dsp():
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)

    g.add_edge("B", "F", 6)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "C", 8)

    g.add_edge("C", "D", 1)

    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)

    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    path = g.dsp("A", "B")
    if path == (2, ['A', 'B']):
        print("path is (2, [A,B])")
    path = g.dsp("A", "C")
    if path == (10, ['A', 'B', 'C']):
        print("path == (10, ['A', 'B', 'C'])")
    path = g.dsp("A", "D")
    if path == (11, ['A', 'B', 'C', 'D']):
        print("path == (11, ['A', 'B', 'C', 'D'])")
    path = g.dsp("A", "F")
    if path == (8, ['A', 'B', 'F']):
        print("path == (8, ['A', 'B', 'F'])")
    path = g.dsp("D","A")
    if path == (math.inf, []):
        print("path == (math.inf, [])")


def main():
    """Tests Graph ADT"""
    """you will do the following:
    1. Construct the graph shown in Figure 1 using your ADT.
    2. Print it to the console in GraphViz notation as shown in Figure 1. 
    3. Print results of DFS starting with vertex “A” as shown in Figure 2.
    4. BFS starting with vertex “A” as shown in Figure 3.
    5. Print the path from vertex “A” to vertex “F” (not shown here) using Djikstra’s 
    shortest path algorithm (DSP) as a string like #3 and #4.
    6. Print the shortest paths from “A” to each other vertex, one path per line using DSP
    """

    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)

    g.add_edge("B", "C", 8)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "F", 6)

    g.add_edge("C", "D", 1)

    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)

    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    print(g)

    print("starting DFS with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end="")
    print()

    print("starting BFS with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end="")
    print()

    # print dsp from A to F

    # print dsp from A to each other vertex. One path per line.
    print(g.dsp("A", "D"))

    # test_vertex_edge_weight()
    # test_print()
    # test_bfs()
    # test_dfs()
    # test_dsp()


if __name__ == "__main__":
    main()
