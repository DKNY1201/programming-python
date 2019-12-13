import unittest
from .UnionFind import UnionFind


def min_cost_to_repair_edges(n, edges, broken_edges):
    if not broken_edges:
        return 0

    # adjust all node by -1 because Union Find start from 0 but given input start from 1
    for e in edges:
        e[0] -= 1
        e[1] -= 1

    for e in broken_edges:
        e[0] -= 1
        e[1] -= 1

    uf = UnionFind(n)
    s = set()

    for e in broken_edges:
        s.add(str(e[0]) + ":" + str(e[1]))

    for e in edges:
        fr, to = e[0], e[1]
        key = str(e[0]) + ":" + str(e[1])

        if key not in s:
            uf.unify(fr, to)

    # no broken edge
    if uf.get_num_of_component() == 1:
        return 0

    broken_edges.sort(key=lambda x: x[2])
    res = 0

    for e in broken_edges:
        fr, to, cost = e[0], e[1], e[2]
        uf.unify(fr, to)
        res += cost

        if uf.get_num_of_component() == 1:
            break

    return res


class Test(unittest.TestCase):
    def test_min_cost_to_repair_edges(self):
        n = 5
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        broken_edges = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
        self.assertEqual(20, min_cost_to_repair_edges(n, edges, broken_edges),
                         "Should return correct minimum cost to repair all broken edges")

        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
        broken_edges = [[1, 6, 410], [2, 4, 800]]
        self.assertEqual(410, min_cost_to_repair_edges(n, edges, broken_edges),
                         "Should return correct minimum cost to repair all broken edges")

        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
        broken_edges = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
        self.assertEqual(79, min_cost_to_repair_edges(n, edges, broken_edges),
                         "Should return correct minimum cost to repair all broken edges")

        n = 6
        edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
        broken_edges = []
        self.assertEqual(0, min_cost_to_repair_edges(n, edges, broken_edges),
                         "Should return 0 when there are no broken edges")
