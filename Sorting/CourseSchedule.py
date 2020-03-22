"""
Problem: https://leetcode.com/problems/course-schedule/

Solution: Basically add all edges to a graph, check if we can do topological sort on this graph by checking is it has
a cycle in it. If has cycle return False, otherwise return True.

We introduce a "path" that stores nodes are on the path we're examining. If we see that node again then we can decide
there is a cycle.
"""
import unittest


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.vertexes = set()

    def add_edge(self, u, v):
        if u not in self.adj_list.keys():
            self.adj_list[u] = []

        self.adj_list[u].append(v)
        self.vertexes.add(u)
        self.vertexes.add(v)

    def add_vertex(self, u):
        self.adj_list[u] = []


def course_schedule(edges, num_courses):
    if not edges:
        return True

    if num_courses <= 0:
        return False

    graph = Graph()

    for edge in edges:
        # nature of input and edge of graph is reverse so need to add [1] then [0]
        graph.add_edge(edge[1], edge[0])

    if num_courses < len(graph.vertexes):
        return False

    # check visited node so no need to re-visit it, prevent infinity recursion
    visited = set()
    # current examining path
    path = set()

    for node in graph.adj_list.keys():
        if node not in visited:
            if not helper(node, visited, path, graph):
                return False

    return True


def helper(start_node, visited, path, graph):
    visited.add(start_node)
    path.add(start_node)

    if start_node in graph.adj_list.keys():
        for neighbor_node in graph.adj_list[start_node]:
            # found cycle, there is a back edge from neighbor_node to a node in examining path
            if neighbor_node in path:
                return False
            if neighbor_node not in visited:
                if not helper(neighbor_node, visited, path, graph):
                    return False

    # backtracking: this node no longer in examining path
    path.remove(start_node)
    return True


class Test(unittest.TestCase):
    def test_course_schedule(self):
        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7]]
        self.assertEqual(course_schedule(edges, 7), True, "Should return correct result")

        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7]]
        self.assertEqual(course_schedule(edges, 8), True,
                         "Should return True when num of courses large than courses need to finish")

        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7], [5, 3]]
        self.assertEqual(course_schedule(edges, 8), False,
                         "Should return False when there is a cycle. 5 -> 2 -> 3 -> 5")

        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7]]
        self.assertEqual(course_schedule(edges, 6), False,
                         "Should return False when num_courses < courses need to finish")

        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7]]
        self.assertEqual(course_schedule(edges, 0), False,
                         "Should return False when num_courses = 0")

        edges = [[2, 1], [3, 2], [4, 3], [2, 5], [1, 6], [3, 7], [5, 6], [6, 7]]
        self.assertEqual(course_schedule(edges, -1), False,
                         "Should return False when num_courses is negative")

        edges = []
        self.assertEqual(course_schedule(edges, 0), True,
                         "Should return True when num_courses is 0 and prerequisite pair is empty")
