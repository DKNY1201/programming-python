import unittest
from collections import deque


def calc_distance_dfs(adj_list, distances, start_node):
    if not adj_list or not distances or not start_node:
        return None

    distances_from_start_node = {}

    for key in adj_list.keys():
        distances_from_start_node[key] = 0

    q = deque([start_node])
    parents = {start_node: None}

    while q:
        cur_node = q.popleft()

        if cur_node != start_node:
            parent = parents.get(cur_node)
            distance = distances.get((parent, cur_node))
            distances_from_start_node[cur_node] = distances_from_start_node[parent] + distance

        for node in adj_list[cur_node]:
            if node not in parents:
                q.append(node)
                parents[node] = cur_node

    return distances_from_start_node


def convert_node_to_val_obj(distances):
    res = dict()

    for distance in distances.keys():
        res[distance.val] = distances[distance]

    return res


class Node:
    def __init__(self, val):
        self.val = val


class Test(unittest.TestCase):

    def test_calc_distance_dfs(self):
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

        self.assertEqual(calc_distance_dfs(adj_list_1, distances_1, node_A), expected_result_1,
                         "Should return a correct distance list start from A")
