"""
There are some islands connected by some bridges. Find the bridges that will disconnect those islands if it's broken
"""

import unittest


class Graph:
    def __init__(self, num_islands):
        self.num_islands = num_islands + 1
        self.adj_list = [[] for i in range(self.num_islands)]
        # time when examine a vertex
        self.time = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_critical_bridges_tarjan(self):
        """
        See more: CriticalRouters.py

        All island that connect together even one of their bridge is broken have same lows value
        A bridge is critical when lows[u] != lows[v]
        """
        if not self.adj_list:
            return []

        # keep track visited vertex
        visited = [0] * self.num_islands
        # keep track time we examine a vertex. ids never change after assign a value
        ids = [float("Inf")] * self.num_islands
        # keep track lowest time of reachable vertex via back edge
        lows = [float("Inf")] * self.num_islands
        # keep track parent of a vertex, root has no parent
        parents = [0] * self.num_islands
        parents[0] = -1
        # result to return
        res = []

        for i in range(self.num_islands):
            if not visited[i]:
                self.dfs(i, visited, ids, lows, parents, res)

        return res

    def dfs(self, u, visited, ids, lows, parents, res):
        visited[u] = 1
        ids[u] = self.time
        lows[u] = self.time
        # increase time for examining next vertex
        self.time += 1

        for v in self.adj_list[u]:
            if not visited[v]:
                parents[v] = u
                self.dfs(v, visited, ids, lows, parents, res)
                # after examine its children, update lows of current vertex
                lows[u] = min(lows[u], lows[v])

                if ids[u] < lows[v]:
                    res.append((u, v))

            elif v != parents[u]:
                # update lows of current vertex
                lows[u] = min(lows[u], ids[v])


class Test(unittest.TestCase):
    def test_find_critical_bridges_tarjan(self):
        graph = Graph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(2, 5)
        graph.add_edge(5, 6)
        graph.add_edge(6, 7)
        graph.add_edge(5, 7)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([(2, 3), (2, 5), (3, 4)], sorted(tuples, key=lambda tup:tup[0]),
                         "Should return correct list of critical bridges")

        graph = Graph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        graph.add_edge(2, 5)
        graph.add_edge(5, 6)
        graph.add_edge(3, 4)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([(2, 5), (3, 4), (5, 6)], sorted(tuples, key=lambda tup: tup[0]),
                         "Should return correct list of critical bridges")

        graph = Graph(5)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([(0, 1), (1, 2), (2, 3), (3, 4)], sorted(tuples, key=lambda tup: tup[0]),
                         "Should return correct list of critical bridges when all islands are on a line")

        graph = Graph(2)
        graph.add_edge(0, 1)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([(0, 1)], sorted(tuples, key=lambda tup: tup[0]),
                         "Should return empty list of critical bridges when there is only 2 islands")

        graph = Graph(0)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([], sorted(tuples, key=lambda tup: tup[0]),
                         "Should return empty list of critical bridges when there is no island")

        graph = Graph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(3, 5)
        graph.add_edge(5, 4)
        tuples = graph.find_critical_bridges_tarjan()
        self.assertEqual([], tuples,
                         "Should return empty list when there is no critical bridge")
