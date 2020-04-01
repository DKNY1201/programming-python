import unittest
from Graph import Graph
import heapq


class MST:
    def __init__(self, g):
        self.g = g
        self.mst_cost = 0
        self.mst_edges = []
        self.solved = False
        # number of vertexes
        self.n = len(g.get_adj_list())
        self.visited = [0] * self.n
        self.pq = []
        self.can_form_mst = False

    def solve_mst(self):
        heapq.heapify(self.pq)
        start_node = 0
        self.handle_node_tasks(start_node)

        # definition of a tree is number of edges = number of vertexes - 1
        while self.pq and len(self.mst_edges) < self.n:
            cost, fr, to = heapq.heappop(self.pq)

            if not self.visited[to]:
                self.mst_edges.append([fr, to])
                self.mst_cost += cost
                self.handle_node_tasks(to)

        if len(self.mst_edges) == self.n - 1:
            self.can_form_mst = True

        self.solved = True

    def handle_node_tasks(self, fr):
        self.visited[fr] = 1

        for to, cost in self.g.get_adj_list()[fr]:
            if not self.visited[to]:
                heapq.heappush(self.pq, (cost, fr, to))

    def get_mst_cost(self):
        if not self.solved:
            self.solve_mst()

        if self.can_form_mst:
            return self.mst_cost

        return -1

    def get_mst_edges(self):
        if not self.solved:
            self.solve_mst()

        if self.can_form_mst:
            return self.mst_edges

        return None


class Test(unittest.TestCase):
    def test_calc_mpt_cost(self):
        g = Graph(8)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 4)
        g.add_edge(1, 4, 0)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(2, 5, 8)
        g.add_edge(3, 5, 2)
        g.add_edge(3, 6, 7)
        g.add_edge(4, 5, 1)
        g.add_edge(4, 7, 8)
        g.add_edge(5, 6, 6)
        g.add_edge(5, 7, 9)
        g.add_edge(6, 7, 12)
        mst = MST(g)
        print(mst.get_mst_edges())
        self.assertEqual(20, mst.get_mst_cost(), "Should return correct minimum cost to construct a minimum spanning tree")

        g = Graph(10)
        g.add_edge(0, 1, 5)
        g.add_edge(0, 4, 1)
        g.add_edge(0, 3, 4)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 3, 2)
        g.add_edge(3, 4, 2)
        g.add_edge(3, 7, 2)
        g.add_edge(3, 6, 11)
        g.add_edge(3, 5, 5)
        g.add_edge(4, 5, 1)
        g.add_edge(5, 6, 7)
        g.add_edge(7, 2, 4)
        g.add_edge(7, 8, 6)
        g.add_edge(7, 6, 1)
        g.add_edge(2, 9, 2)
        g.add_edge(8, 2, 1)
        g.add_edge(8, 9, 0)
        g.add_edge(8, 6, 4)
        mst = MST(g)
        print(mst.get_mst_edges())
        self.assertEqual(14, mst.get_mst_cost(), "Should return correct minimum cost to construct a minimum spanning tree")

        g = Graph(3)
        g.add_edge(0, 1, 1)
        mst = MST(g)
        print(mst.get_mst_edges())
        self.assertEqual(-1, mst.get_mst_cost(), "Should return -1 when can NOT construct a minimum spanning tree")