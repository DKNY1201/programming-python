"""
https://leetcode.com/problems/number-of-islands/
"""
import unittest


def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0

    res = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                res += 1
                dfs(grid, r, c)

    return res


def dfs(grid, r, c):
    if is_safe(grid, r, c):
        grid[r][c] = "2"
        dfs(grid, r + 1, c)
        dfs(grid, r - 1, c)
        dfs(grid, r, c + 1)
        dfs(grid, r, c - 1)


def is_safe(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
        return False

    return True


class Test(unittest.TestCase):
    def test_num_islands(self):
        grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]]
        self.assertEqual(1, num_islands(grid), "Should return correct number of islands")

        grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]]
        self.assertEqual(3, num_islands(grid), "Should return correct number of islands")

        grid = []
        self.assertEqual(0, num_islands(grid), "Should return 0 if grid is empty")