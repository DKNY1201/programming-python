import unittest
from .UnionFind import UnionFind


def calc_mpt_cost(edges, n):
    edges = transform_edge_to_nums(edges)

    res = 0
    edges.sort(key=lambda edge: edge[2])
    uf = UnionFind(n)

    for edge in edges:
        fr, to, cost = edge[0], edge[1], edge[2]

        if uf.is_connected(fr, to):
            continue

        res += cost
        uf.unify(fr, to)

        if uf.get_num_of_component() == 1:
            break

    # no MST available
    if uf.get_component_size(0) != n:
        return -1

    return res


def transform_edge_to_nums(edges):
    vertices = set()
    map = {}

    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])

    for idx, vertex in enumerate(vertices):
        map[vertex] = idx

    for edge in edges:
        edge[0] = map[edge[0]]
        edge[1] = map[edge[1]]

    return edges


class Test(unittest.TestCase):
    def test_calc_mpt_cost(self):
        edges = [
            # from, to, cost
            ["A", "B", 5],
            ["A", "E", 1],
            ["A", "D", 4],
            ["B", "C", 4],
            ["B", "D", 2],
            ["D", "E", 2],
            ["D", "H", 2],
            ["D", "G", 11],
            ["D", "F", 5],
            ["E", "F", 1],
            ["F", "G", 7],
            ["H", "C", 4],
            ["H", "I", 6],
            ["H", "G", 1],
            ["C", "J", 2],
            ["I", "C", 1],
            ["I", "J", 0],
            ["I", "G", 4],
        ]
        n = 10
        self.assertEqual(14, calc_mpt_cost(edges, n), "Should return correct minimum cost to construct spanning tree")
