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
