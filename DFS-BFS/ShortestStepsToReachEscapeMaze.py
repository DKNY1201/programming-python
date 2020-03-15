import unittest
from collections import deque


def solution(A, sr, sc):
    q = deque([])
    q.append((sr, sc, 0))
    visited = [[0] * len(A[0]) for i in range(len(A))]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while q:
        r, c, lvl = q.popleft()

        if A[r][c] == 'E':
            return lvl

        visited[r][c] = 1
        examine_neighbors(A, visited, q, r, c, lvl, dr, dc)

    return -1


def examine_neighbors(A, visited, q, r, c, lvl, dr, dc):
    for i in range(len(dr)):
        new_r = r + dr[i]
        new_c = c + dc[i]

        if new_r < 0 or new_r >= len(A) or new_c < 0 or new_c >= len(A[0]) or A[new_r][new_c] == '#' or visited[new_r][new_c]:
            continue

        q.append((new_r, new_c, lvl + 1))


class Test(unittest.TestCase):
    def test_solution(self):
        grid = [['.', '.', '.', '#', '.', '.', '.'],
                ['.', '#', '.', '.', '.', '#', '.'],
                ['.', '#', '.', '.', '.', '.', '.'],
                ['.', '.', '#', '#', '.', '.', '.'],
                ['#', '.', '#', 'E', '.', '#', '.']]

        self.assertEqual(9, solution(grid, 0, 0),
                         "Should return correct shortest steps escape the maze")

        grid = [['.', '.', '.', '#', '.', '.', '.'],
                ['.', '#', '.', '.', '.', '#', '.'],
                ['.', '#', '.', '.', '.', '.', '.'],
                ['.', '.', '#', '#', '#', '.', '.'],
                ['#', '.', '#', 'E', '.', '#', '.']]

        self.assertEqual(-1, solution(grid, 0, 0),
                         "Should return -1 if there is no way to escape the maze")