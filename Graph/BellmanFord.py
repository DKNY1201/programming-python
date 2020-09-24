import unittest
import sys


def shortest_path_bellman_ford(graph, s):
    """
        Calculate shortest values and shortest paths from given graph and start vertex using Bellman Ford algorithms.
        @:param graph: graph to examine
        @:param s: start point
        @:return: tuple of shortest values and shortest paths if there is no negative cycle otherwise return None
    """
    s_vals = {}
    s_paths = {}

    # All nodes will have Infinity distance at first since we don't know we can reach to them yet. Start node distance
    # is 0 since we already on it
    for node in graph.vertexes:
        s_vals[node] = sys.maxsize
        s_paths[node] = None
    s_vals[s] = 0

    # updated all edges V (number of vertexes) times
    # we need to run V times because we examine edges in randomize order. In some cases we will run from Infinity cost
    # node to another Infinity cost node so run in V times will make sure all nodes in s_vals will have correct cost
    for i in range(len(graph.vertexes)):
        is_any_distance_updated = False

        for edge in graph.edges:
            src, dest, weight = edge["src"], edge["dest"], edge["weight"]

            if s_vals[dest] > s_vals[src] + weight:
                is_any_distance_updated = True
                s_vals[dest] = s_vals[src] + weight
                s_paths[dest] = src

        # if no distance was updated so we already have best distances for all nodes
        if not is_any_distance_updated:
            break

    # check for negative cycle in graph.
    # the s_paths in above loop presume we got the shortest path. If we can update any path then we find negative cycle
    for edge in graph.edges:
        src, dest, weight = edge["src"], edge["dest"], edge["weight"]

        if s_vals[src] + weight < s_vals[dest]:
            return None

    return s_vals, s_paths


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edges = []
        self.vertexes = set()

    def add_edge(self, u, v, w):
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

        self.adj_list[u].append((v, w))
        self.edges.append({
            "src": u,
            "dest": v,
            "weight": w
        })
        self.vertexes.add(u)
        self.vertexes.add(v)

    def add_vertex(self, u):
        self.adj_list[u] = []


class Test(unittest.TestCase):
    def test_shortest_path_dijkstra(self):
        graph = Graph()
        graph.add_edge("A", "B", 4)
        graph.add_edge("A", "H", 8)
        graph.add_edge("B", "A", 4)
        graph.add_edge("B", "H", 11)
        graph.add_edge("B", "C", 8)
        graph.add_edge("C", "B", 8)
        graph.add_edge("C", "D", 7)
        graph.add_edge("C", "F", 4)
        graph.add_edge("C", "I", 2)
        graph.add_edge("D", "C", 7)
        graph.add_edge("D", "F", 14)
        graph.add_edge("D", "E", 9)
        graph.add_edge("E", "D", 9)
        graph.add_edge("E", "F", 10)
        graph.add_edge("F", "C", 4)
        graph.add_edge("F", "D", 14)
        graph.add_edge("F", "E", 10)
        graph.add_edge("F", "G", 2)
        graph.add_edge("G", "F", 2)
        graph.add_edge("G", "I", 6)
        graph.add_edge("G", "H", 1)
        graph.add_edge("H", "A", 8)
        graph.add_edge("H", "B", 11)
        graph.add_edge("H", "I", 7)
        graph.add_edge("H", "G", 1)
        graph.add_edge("I", "C", 2)
        graph.add_edge("I", "H", 7)
        graph.add_edge("I", "G", 6)
        s_vals, s_paths = shortest_path_bellman_ford(graph, "A")
        expected_s_vals = {
            "A": 0,
            "B": 4,
            "C": 12,
            "D": 19,
            "E": 21,
            "F": 11,
            "G": 9,
            "H": 8,
            "I": 14,
        }
        expected_s_paths = {
            "A": None,
            "B": "A",
            "C": "B",
            "D": "C",
            "E": "F",
            "F": "G",
            "G": "H",
            "H": "A",
            "I": "C",
        }
        self.assertEqual(expected_s_vals, s_vals, "Should return correct shortest values")
        self.assertEqual(expected_s_paths, s_paths, "Should return correct shortest paths")

        graph1 = Graph()
        graph1.add_edge("A", "B", 1)
        graph1.add_edge("B", "C", 2)
        graph1.add_edge("C", "E", 1)
        graph1.add_edge("C", "D", -4)
        graph1.add_edge("D", "B", 1)
        self.assertEqual(None, shortest_path_bellman_ford(graph1, "A"),
                         "Should return None if graph contains negative cycle")
