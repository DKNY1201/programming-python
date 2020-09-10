import unittest
from collections import deque


def topological_sort_kahn(edges, n):
    # build adjacent list
    adjs = [[] for _ in range(n)]
    in_degree_list = [0] * n

    for fr, to in edges:
        adjs[fr].append(to)
        in_degree_list[to] += 1

    q = deque([])
    result = []

    # add zero in degree nodes to queue
    for i, in_degree in enumerate(in_degree_list):
        if in_degree == 0:
            q.append(i)

    # examine the queue
    while q:
        zero_in_degree_node = q.popleft()
        result.append(zero_in_degree_node)

        for neighbor in adjs[zero_in_degree_node]:
            in_degree_list[neighbor] -= 1

            if in_degree_list[neighbor] == 0:
                q.append(neighbor)

    # circle found
    if len(result) != n:
        return []

    return result


class Test(unittest.TestCase):
    def test_topological_sort_kahn(self):
        edges = [[0, 2], [0, 3], [0, 6], [1, 4], [2, 6], [3, 1], [3, 4], [4, 5], [4, 8], [6, 7], [6, 11], [7, 4], [7, 12], [9, 2], [9, 10], [10, 6], [11, 12]]
        self.assertEqual([0, 9, 13, 3, 2, 10, 1, 6, 7, 11, 4, 12, 5, 8], topological_sort_kahn(edges, 14),
                         "Should return topological sort order")

        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual([0, 1, 2, 3, 4], topological_sort_kahn(edges, 5), "Should return topological sort order")

        edges = [[1, 0], [2, 1], [2, 4], [3, 0], [3, 1], [3, 4], [4, 0]]
        self.assertEqual([2, 3, 1, 4, 0], topological_sort_kahn(edges, 5), "Should return topological sort order")

        edges = [[0, 1], [1, 2], [2, 0]]
        self.assertEqual([], topological_sort_kahn(edges, 3),
                         "Should return empty array since there is a circle in the graph")

        edges = [[0, 1], [1, 2], [2, 3], [3, 1]]
        self.assertEqual([], topological_sort_kahn(edges, 4),
                         "Should return empty array since there is a circle in the graph")
