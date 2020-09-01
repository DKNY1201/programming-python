import unittest
from collections import deque


def find_shortest_path_from_start_to_end(edges, n, start, end):
    parents = [None] * n
    visited = [0] * n
    visited[start] = 1
    q = deque([start])
    g = build_adjs_list(edges, n)

    while q:
        u = q.popleft()

        for v in g[u]:
            if not visited[v]:
                visited[v] = 1
                parents[v] = u
                q.append(v)

                if v == end:
                    q = None
                    break

    path = []

    while end is not None:
        path.append(end)
        end = parents[end]

    path.reverse()

    return path


def build_adjs_list(edges, n):
    adjs = [[] for _ in range(n)]

    for u, v in edges:
        adjs[u].append(v)
        adjs[v].append(u)

    return adjs


class Test(unittest.TestCase):
    def test_find_shortest_path_from_start_to_end(self):
        edges = [[0, 2], [0, 1], [1, 3], [2, 4], [2, 3], [4, 3], [4, 6], [6, 7], [3, 5], [1, 7], [5, 7]]
        self.assertEqual([0, 1, 7], find_shortest_path_from_start_to_end(edges, 8, 0, 7),
                         "Should return correct shortest path from start to end")

        edges = [[0, 2], [0, 1], [1, 3], [2, 4], [2, 3], [4, 3], [4, 6], [6, 7], [3, 5], [1, 7], [5, 7]]
        self.assertEqual([6,7,5], find_shortest_path_from_start_to_end(edges, 8, 6, 5),
                         "Should return correct shortest path from start to end")

