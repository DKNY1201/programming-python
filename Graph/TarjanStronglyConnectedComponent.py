import unittest


class SCC:
    def build_graph(self, edges, n):
        graph = [[] for _ in range(n)]

        for fr, to in edges:
            graph[fr].append(to)

        return graph

    def get_strongly_connected_components(self, edges, n):
        graph = self.build_graph(edges, n)
        low_link = [0] * n
        ids = [-1] * n
        sccs = []
        on_stack = [0] * n
        stack = []

        for i in range(n):
            if ids[i] == -1:
                self.dfs(graph, i, ids, low_link, sccs, stack, on_stack, 0)

        return sccs

    def dfs(self, graph, node, ids, low_link, sccs, stack, on_stack, id):
        ids[node] = id
        low_link[node] = id
        on_stack[node] = 1
        stack.append(node)

        for neighbor in graph[node]:
            if ids[neighbor] == -1:
                self.dfs(graph, neighbor, ids, low_link, sccs, stack, on_stack, id + 1)

            if on_stack[node]:
                low_link[node] = min(low_link[node], low_link[neighbor])

        if ids[node] == low_link[node]:
            scc = []

            while stack[-1] != node:
                pop_node = stack.pop()
                on_stack[pop_node] = 0
                scc.append(pop_node)

            scc.append(stack.pop())
            sccs.append(scc)


class Test(unittest.TestCase):
    def test_shortest_path_dijkstra(self):
        scc = SCC()
        edges = [[0, 1], [1, 6], [6, 0], [1, 4], [1, 2], [2, 3], [3, 2], [5, 2], [5, 3], [5, 4], [4, 5]]
        expected_value = [[3, 2], [5, 4], [6, 1, 0]]
        sccs = scc.get_strongly_connected_components(edges, 7)

        self.assertEqual(expected_value, sccs, "Should return correct strongly connected components")
        self.assertEqual(3, len(sccs), "Should return correct number of strongly connected components")
