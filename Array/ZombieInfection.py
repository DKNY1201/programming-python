import unittest
from collections import deque


def zombie_infection(A):
    if not A:
        return -1

    q = deque([])
    # divide each infection, increase hour by one when encounter divider
    divider = "|"
    res = 0
    n, m = len(A), len(A[0])

    # put all zombies into queue
    for r in range(n):
        for c in range(m):
            if A[r][c] == 1:
                q.append((r, c))

    # no zombie
    if not q:
        return -1

    q.append(divider)

    while q:
        coor = q.popleft()

        if coor == divider:
            # stop when no human to infect
            if len(q) == 0:
                break

            res += 1
            q.append(divider)
        else:
            # infect
            r, c = coor

            if r > 0 and A[r - 1][c] != 1:
                q.append((r - 1, c))
                A[r - 1][c] = 1

            if r < n - 1 and A[r + 1][c] != 1:
                q.append((r + 1, c))
                A[r + 1][c] = 1

            if c > 0 and A[r][c - 1] != 1:
                q.append((r, c - 1))
                A[r][c - 1] = 1

            if c < m - 1 and A[r][c + 1] != 1:
                q.append((r, c + 1))
                A[r][c + 1] = 1

    return res


class Test(unittest.TestCase):
    def test_zombie_infection(self):
        A = [
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0],
        ]
        self.assertEqual(2, zombie_infection(A), "Should return a correct minute to infect all human")

        A = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(7, zombie_infection(A), "Should return a correct minute to infect all human")

        A = []
        self.assertEqual(-1, zombie_infection(A), "Should return -1 if there is no zombie or human")

        A = [[0]]
        self.assertEqual(-1, zombie_infection(A), "Should return -1 if there are all human")

        A = [[1]]
        self.assertEqual(0, zombie_infection(A), "Should return 0 if there are all zombie")