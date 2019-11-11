"""
AWS wants to increase the reliability of their network by upgrading crucial data center routers. Each data center has a single router that is connected to every other data center through a direct link or some other data center.

To increase the fault tolerance of the network, AWS wants to identify routers which would result in a disconnected network if they went down and replace then with upgraded versions.

Write an algorithm to identify all such routers.

Input:

The input to the function/method consists of three arguments:

numRouters, an integer representing the number of routers in the data center.
numLinks, an integer representing the number of links between the pair of routers.
Links, the list of pair of integers - A, B representing a link between the routers A and B. The network will be connected.
Output:

Return a list of integers representing the routers with need to be connected to the network all the time.

Example:

Input:

numRouters = 7
numLinks = 7
Links = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]

Output:

[2, 3, 5]

Explanation:

On disconnecting router 2, a packet may be routed either to the routers- 0, 1, 3, 4 or the routers - 5, 6, but not to all.

On disconnecting router 3, a packet may be routed either to the routers - 0,1,2,5,6 or to the router - 4, but not to all.

On disconnecting router 5, a packet may be routed either to the routers - 0,1,2,3,4 or to the router - 6, but not to all.
"""

import unittest
from collections import deque


class Router:
    def __init__(self, val):
        self.val = val
        self.links = []

    def add_links(self, router):
        self.links.append(router)


def get_critical_routers(num_routers, links):
    """
    Idea is loop through all routers. For each loop start from any router, run the DFS and prevent current router.
    Check for number of visited routers, if it is less than number of (all routers - 1) then it is critical router
    """
    if not num_routers:
        return []

    if num_routers == 1:
        return [0]

    routers = [Router(i) for i in range(num_routers)]
    res = []

    for link in links:
        routers[link[0]].links.append(link[1])
        routers[link[1]].links.append(link[0])

    for i in range(num_routers):
        is_critical_router = dfs(0, i, routers, num_routers) if i != 0 else dfs(1, 0, routers, num_routers)

        if is_critical_router:
            res.append(i)

    return res


def dfs(start_router, prevent_router, routers, num_routers):
    q = deque()
    q.append(routers[start_router])
    visited = set()

    while q:
        router = q.popleft()
        router_links = router.links
        visited.add(router.val)

        for sibling_router in router_links:
            if sibling_router != prevent_router and sibling_router not in visited:
                q.append(routers[sibling_router])

    return len(visited) < num_routers - 1


class Graph:
    def __init__(self, num_routers):
        self.num_routers = num_routers + 1
        self.adj_list = [[] for i in range(self.num_routers)]
        # time when examine a vertex
        self.time = 0

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_critical_router_tarjan(self):
        """
        A vertex is critical vertex iff it satisfies one of following condition
        - If vertex is root and has more than 2 children
        - If vertex is not root and no back edges from its children to its ancestors

        Note:
        - To have ancestor -> descendant, use DFS
        - To identify a back edge, store the time we examine a vertex. If we encounter a vertex v again from a vertex u
        then there is a back edge from u -> v
        """
        if not self.adj_list:
            return []

        # keep track visited vertex
        visited = [0] * self.num_routers
        # keep track time we examine a vertex. ids never change after assign a value
        ids = [float("Inf")] * self.num_routers
        # keep track lowest time of reachable vertex via back edge
        lows = [float("Inf")] * self.num_routers
        # keep track parent of a vertex, root has no parent
        parents = [0] * self.num_routers
        parents[0] = -1
        # result to return
        res = [0] * self.num_routers

        for i in range(self.num_routers):
            if not visited[i]:
                self.dfs(i, visited, ids, lows, parents, res)

        return [idx for idx, i in enumerate(res) if i == 1]

    def dfs(self, u, visited, ids, lows, parents, res):
        visited[u] = 1
        ids[u] = self.time
        lows[u] = self.time
        num_child = 0
        # increase time for examining next vertex
        self.time += 1

        for v in self.adj_list[u]:
            num_child += 1

            if not visited[v]:
                parents[v] = u
                self.dfs(v, visited, ids, lows, parents, res)
                # after examine its children, update lows of current vertex
                lows[u] = min(lows[u], lows[v])

                # if root
                if parents[u] == -1:
                    # has more than 2 children
                    if num_child >= 2:
                        res[u] = 1
                # else if current examine time less than low of its children. In other words, no back edge
                elif ids[u] <= lows[v]:
                    res[u] = 1

            elif v != parents[u]:
                # update lows of current vertex
                lows[u] = min(lows[u], ids[v])


class Test(unittest.TestCase):
    def test_get_max(self):
        num_routers = 7
        links = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        self.assertEqual([2, 3, 5], get_critical_routers(num_routers, links),
                         "Should return correct list of critical routers")

        num_routers = 5
        links = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual([1, 2, 3], get_critical_routers(num_routers, links),
                         "Should return correct list of critical routers when all routers are on a line")

        num_routers = 1
        links = []
        self.assertEqual([0], get_critical_routers(num_routers, links),
                         "Should return correct list of critical routers when there is only 1 router")

        num_routers = 0
        links = []
        self.assertEqual([], get_critical_routers(num_routers, links),
                         "Should return empty list of critical routers when there is no router")

    def test_find_critical_router_tarjan(self):
        graph = Graph(7)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        graph.add_edge(2, 5)
        graph.add_edge(5, 6)
        graph.add_edge(6, 7)
        graph.add_edge(5, 7)
        self.assertEqual([2, 3, 5], sorted(graph.find_critical_router_tarjan()),
                         "Should return correct list of critical routers")

        graph = Graph(6)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 3)
        graph.add_edge(2, 5)
        graph.add_edge(5, 6)
        graph.add_edge(3, 4)
        self.assertEqual([2, 3, 5], sorted(graph.find_critical_router_tarjan()),
                         "Should return correct list of critical routers")

        graph = Graph(5)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(3, 4)
        self.assertEqual([1, 2, 3], sorted(graph.find_critical_router_tarjan()),
                         "Should return correct list of critical routers when all routers are on a line")

        graph = Graph(2)
        graph.add_edge(0, 1)
        self.assertEqual([], sorted(graph.find_critical_router_tarjan()),
                         "Should return empty list of critical routers when there is only 2 router")

        graph = Graph(0)
        self.assertEqual([], sorted(graph.find_critical_router_tarjan()),
                         "Should return empty list of critical routers when there is no router")
