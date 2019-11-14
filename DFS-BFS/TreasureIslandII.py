"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
"""

import unittest
from collections import deque


def calc_shortest_steps_explorer_find_treasure_island(grid):
    q = deque(get_explorers_coordinate(grid))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    distance = 0

    while q:
        num_current_coors_in_q = len(q)
        for i in range(num_current_coors_in_q):
            x, y = q.popleft()
            grid[x][y] = "D"

            for dir in directions:
                new_x, new_y = dir[0] + x, dir[1] + y

                if is_safe(grid, new_x, new_y):
                    if grid[new_x][new_y] == "X":
                        return distance + 1

                    q.append((new_x, new_y))

        distance += 1

    return -1


def is_safe(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "D"


def get_explorers_coordinate(grid):
    coors = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                coors.append((r, c))
                grid[r][c] = "D"

    return coors


class Test(unittest.TestCase):
    def test_calc_shortest_steps_explorer_find_treasure_island(self):
        grid = [['S', 'O', 'O', 'S', 'S'],
                ['D', 'O', 'D', 'O', 'D'],
                ['O', 'O', 'O', 'O', 'X'],
                ['X', 'D', 'D', 'O', 'O'],
                ['X', 'D', 'D', 'D', 'O']]

        self.assertEqual(3, calc_shortest_steps_explorer_find_treasure_island(grid),
                         "Should return correct shortest steps to find treasure island")

        grid = [['S', '0', 'O', 'S', 'S'],
                ['D', 'X', 'D', 'O', 'D'],
                ['O', 'O', 'O', 'O', 'X'],
                ['X', 'D', 'D', 'O', 'O'],
                ['X', 'D', 'D', 'D', 'O']]

        self.assertEqual(2, calc_shortest_steps_explorer_find_treasure_island(grid),
                         "Should return correct shortest steps to find treasure island")