import heapq
import unittest


def shortest_path_dijkstra(graph, s):
    """
        Calculate shortest values and shortest paths from given graph and start vertex.
        @:param graph: graph to examine
        @:param s: start point
        @:return: tuple of shortest values and shortest paths
    """
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (0, s))

    s_vals = {s: 0}
    s_paths = {s: None}
    visited = set()

    while pq:
        min = heapq.heappop(pq)
        min_dist = min[0]
        min_node = min[1]

        # no need to examine visited node. This happen because we don't have properly decrease key func in
        # priority queue. We just add decreased key to pq
        if min_node in visited:
            continue

        visited.add(min_node)

        for neighbor in graph.adj_list[min_node]:
            neighbor_node = neighbor[0]
            neighbor_dist = neighbor[1]

            if neighbor_node in visited:
                continue

            dist_from_min_node = min_dist + neighbor_dist

            if neighbor_node not in s_vals or dist_from_min_node < s_vals[neighbor_node]:
                s_vals[neighbor_node] = dist_from_min_node
                heapq.heappush(pq, (dist_from_min_node, neighbor_node))
                s_paths[neighbor_node] = min_node

    return s_vals, s_paths


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.vertexes = set()

    def add_edge(self, u, v, w):
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

        self.adj_list[u].append((v, w))
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
        s_vals, s_paths = shortest_path_dijkstra(graph, "A")

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
