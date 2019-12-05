"""
https://leetcode.com/problems/spiral-matrix-ii/
"""
import unittest


def generate_spiral_matrix(n):
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    res = [[0 for i in range(n)] for i in range(n)]
    visited = [[0 for i in range(n)] for i in range(n)]
    # top, right, left, bottom
    dirs = [(-1, 0, "t"), (0, 1, "r"), (1, 0, "b"), (0, -1, "l")]
    dfs(res, visited, dirs, 0, n**2, 0, 0)

    return res


def dfs(res, visited, dirs, n, N, r, c):
    if n == N:
        return

    res[r][c] = n + 1
    visited[r][c] = 1

    next_dir = get_next_dir(visited, r, c, dirs)
    y, x = 0, 0

    if next_dir:
        y = next_dir[0]
        x = next_dir[1]
    # examine next proper coordinate
    dfs(res, visited, dirs, n + 1, N, r + y, c + x)


def get_next_dir(visited, r, c, dirs):
    safe_dirs = []

    for dir in dirs:
        y, x = dir[0], dir[1]
        if is_safe(visited, r + y, c + x):
            safe_dirs.append(dir)

    if len(safe_dirs) == 1:
        return safe_dirs[0]
    # observe and we can get:
    # - If we can go top and right then choose top
    # - If we can go right and bottom then choose right
    # - If we can go top and left then choose left
    # - If we can go bottom and left then choose bottom
    elif len(safe_dirs) == 2:
        if safe_dirs[0][2] == "t" and safe_dirs[1][2] == "r":
            return safe_dirs[0]
        elif safe_dirs[0][2] == "r" and safe_dirs[1][2] == "b":
            return safe_dirs[0]
        elif safe_dirs[0][2] == "t" and safe_dirs[1][2] == "l":
            return safe_dirs[1]
        elif safe_dirs[0][2] == "b" and safe_dirs[1][2] == "l":
            return safe_dirs[0]


def is_safe(visited, r, c):
    return 0 <= r < len(visited) and 0 <= c < len(visited[0]) and not visited[r][c]


class Test(unittest.TestCase):
    def test_generate_spiral_matrix(self):
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(expected, generate_spiral_matrix(3),
                         "Should return correct spiral matrix for given input")

        expected = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
        self.assertEqual(expected, generate_spiral_matrix(5),
                         "Should return correct spiral matrix for given input")

        expected = []
        self.assertEqual(expected, generate_spiral_matrix(0),
                         "Should return empty matrix for given input as 0")

        expected = [[1]]
        self.assertEqual(expected, generate_spiral_matrix(1),
                         "Should return matrix with single element for given input as 1")
