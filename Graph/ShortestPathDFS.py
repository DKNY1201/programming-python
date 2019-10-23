import unittest
from collections import deque


def shortest_path_dfs(adj_list, distances, start_node):
    if not adj_list or not distances or not start_node:
        return None

    shortest_distance = {}

    for key in adj_list.keys():
        shortest_distance[key] = 0

    q = deque([start_node])
    parents = {start_node: None}
    visited = set()

    while q:
        cur_node = q.popleft()
        visited.add(cur_node)

        if cur_node != start_node:
            parent = parents.get(cur_node)
            distance = distances.get((parent, cur_node))
            shortest_distance[cur_node] = shortest_distance[parent] + distance

        for node in adj_list[cur_node]:
            if node not in visited:
                parents[node] = cur_node
                q.append(node)

    return shortest_distance


class Node:
    def __init__(self, val):
        self.val = val


node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")

adj_list_1 = {
    node_A: [node_B, node_C],
    node_B: [node_A, node_C],
    node_C: [node_B, node_D],
    node_D: [node_C, node_E],
    node_E: [node_D, node_F],
    node_F: [node_E, node_G, node_H],
    node_G: [node_F, node_H],
    node_H: [node_F, node_G],
}

distances_1 = {
    (node_A, node_B): 1,
    (node_A, node_C): 2,
    (node_B, node_C): 4,
    (node_C, node_D): 2,
    (node_D, node_E): 1,
    (node_E, node_F): 6,
    (node_F, node_G): 2,
    (node_G, node_H): 3,
    (node_F, node_H): 4,
}

expected_result_1 = {
    node_A: 0,
    node_B: 1,
    node_C: 2,
    node_D: 4,
    node_E: 5,
    node_F: 11,
    node_G: 13,
    node_H: 15,
}

res = shortest_path_dfs(adj_list_1, distances_1, node_A)
print(str(res))

# class Test(unittest.TestCase):
#
#     def test_shortest_path_dfs(self):
#         node_A = Node("A")
#         node_B = Node("B")
#         node_C = Node("C")
#         node_D = Node("D")
#         node_E = Node("E")
#         node_F = Node("F")
#         node_G = Node("G")
#         node_H = Node("H")
#
#         adj_list_1 = {
#             node_A: [node_B, node_C],
#             node_B: [node_A, node_C],
#             node_C: [node_B, node_D],
#             node_D: [node_C, node_E],
#             node_E: [node_D, node_F],
#             node_F: [node_E, node_G, node_H],
#             node_G: [node_F, node_H],
#             node_H: [node_F, node_G],
#         }
#
#         distances_1 = {
#             (node_A, node_B): 1,
#             (node_A, node_C): 2,
#             (node_B, node_C): 4,
#             (node_C, node_D): 2,
#             (node_D, node_E): 1,
#             (node_E, node_F): 6,
#             (node_F, node_G): 2,
#             (node_G, node_H): 3,
#             (node_F, node_H): 4,
#         }
#
#         expected_result_1 = {
#             node_A: 0,
#             node_B: 1,
#             node_C: 2,
#             node_D: 4,
#             node_E: 5,
#             node_F: 11,
#             node_G: 13,
#             node_H: 15,
#         }
#
#         self.assertIn(shortest_path_dfs(adj_list_1, distances_1, node_A), expected_result_1,
#                       "Should return a correct shortest distance list start from A")
