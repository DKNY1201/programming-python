import unittest
from .UnionFind import UnionFind


def min_cost_to_connect_all_nodes(n, edges, new_edges):
    if not new_edges:
        return 0

    # adjust all node by -1 because Union Find start from 0 but given input start from 1
    for e in edges:
        e[0] -= 1
        e[1] -= 1

    for e in new_edges:
        e[0] -= 1
        e[1] -= 1

    uf = UnionFind(n)

    # Unify all current vertices
    for e in edges:
        uf.unify(e[0], e[1])

    # If all vertices are connected then just return 0
    if uf.get_num_of_component() == 1:
        return 0

    # Sort new edges to apply Krusal MST algorithms
    new_edges.sort(key=lambda e: e[2])
    res = 0

    for e in new_edges:
        fr, to, cost = e[0], e[1], e[2]

        # Skip if already connected
        if uf.is_connected(fr, to):
            continue

        res += cost
        # Unify 2 unconnected components
        uf.unify(fr, to)

        # all nodes are connected
        if uf.get_num_of_component() == 1:
            break

    return res


class Test(unittest.TestCase):
    def test_min_cost_to_connect_all_nodes(self):
        n = 6
        edges = [[1, 4], [4, 5], [2, 3]]
        new_edges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
        self.assertEqual(7, min_cost_to_connect_all_nodes(n, edges, new_edges),
                         "Should return correct minimum cost to connect all nodes")
