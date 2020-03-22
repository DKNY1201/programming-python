import unittest

"""
Graph must be a DAG (directed acyclic graph), basically a directed graph with no cycle
1. Start with a random node in graph
2. Go to the end of the path that starts from above node. If current node has no un-visited adjacent nodes then add it 
to the stack. Doing this will make sure node that has no dependent nodes on it is added to stack.
3. Repeat step 1, 2 until no un-visited nodes
4. Return reversed stack
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

        self.adj_list[u].append(v)

    def add_vertex(self, u):
        self.adj_list[u] = []

    def topological_sort(self):
        visited = set()
        stack = []

        for node in self.adj_list.keys():
            if node not in visited:
                self.helper(visited, stack, node)

        stack.reverse()

        return stack

    def helper(self, visited, stack, node):
        visited.add(node)
        # DFS traversal
        if node in self.adj_list.keys():
            for adj_node in self.adj_list[node]:
                if adj_node not in visited:
                    self.helper(visited, stack, adj_node)

        # when all adjacent nodes are visited, add it to stack
        stack.append(node)


class Test(unittest.TestCase):

    def test_topological_sort(self):
        graph = Graph()
        graph.add_edge("G", "H")
        graph.add_edge("A", "H")
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "F")
        graph.add_edge("D", "E")
        graph.add_edge("E", "F")
        graph.add_vertex("I")
        expected_result = ["I", "D", "E", "A", "B", "C", "F", "G", "H"]
        self.assertEqual(graph.topological_sort(), expected_result,
                         "Should return correct result for string topological sort")

        graph1 = Graph()
        graph1.add_edge(5, 0)
        graph1.add_edge(5, 2)
        graph1.add_edge(2, 3)
        graph1.add_edge(3, 1)
        graph1.add_edge(4, 0)
        graph1.add_edge(4, 1)
        expected_result_1 = [4, 5, 2, 3, 1, 0]
        self.assertEqual(graph1.topological_sort(), expected_result_1,
                         "Should return correct result for number topological sort")
