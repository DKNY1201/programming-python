"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
"""

import unittest
from collections import deque


def calc_shortest_steps_to_treasure_island(grid):
    if not grid:
        return -1

    # each item in queue is coordinate and distance from start island to treasure island
    q = deque([((0, 0), 0)])
    visited = set()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        item = q.popleft()
        x = item[0][0]
        y = item[0][1]
        distance = item[1]
        visited.add(item[0])

        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if is_safe(grid, new_x, new_y, visited):
                if grid[new_x][new_y] == 'X':
                    return distance + 1

                q.append(((new_x, new_y), distance + 1))

    return -1


def is_safe(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 'D' or (x, y) in visited:
        return False

    return True


class Test(unittest.TestCase):
    def test_calc_shortest_steps_to_treasure_island(self):
        grid = [['O', 'O', 'O', 'O'],
                ['D', 'O', 'D', 'O'],
                ['O', 'O', 'O', 'O'],
                ['X', 'D', 'D', 'O']]

        self.assertEqual(5, calc_shortest_steps_to_treasure_island(grid),
                         "Should return correct shortest steps to find treasure island")

        grid = [['O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O'],
                ['O', 'O', 'O', 'O'],
                ['O', 'O', 'D', 'O'],
                ['D', 'O', 'X', 'O']]

        self.assertEqual(6, calc_shortest_steps_to_treasure_island(grid),
                         "Should return correct shortest steps to find treasure island")
