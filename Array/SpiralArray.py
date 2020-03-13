import unittest


def solution(n):
    if n == 0:
        return []

    res = [[0] * n for i in range(n)]
    dir = "right"
    r = 0
    c = 0

    for i in range(1, n ** 2 + 1):
        res[r][c] = i

        if dir == "right":
            c += 1

            if c == n or res[r][c] != 0:
                c -= 1
                r += 1
                dir = "down"
        elif dir == "down":
            r += 1

            if r == n or res[r][c] != 0:
                r -= 1
                c -= 1
                dir = "left"
        elif dir == "left":
            c -= 1

            if c < 0 or res[r][c] != 0:
                c += 1
                r -= 1
                dir = "top"
        else:
            r -= 1

            if r < 0 or res[r][c] != 0:
                r += 1
                c += 1
                dir = "right"

    return res


class Test(unittest.TestCase):
    def test_zombie_infection(self):
        A = []
        self.assertEqual(A, solution(0), "Should return a spiral array with corresponding input")

        A = [[1]]
        self.assertEqual(A, solution(1), "Should return a spiral array with corresponding input")

        A = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ]
        self.assertEqual(A, solution(3), "Should return a spiral array with corresponding input")

        A = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        self.assertEqual(A, solution(4), "Should return a spiral array with corresponding input")

        A = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        self.assertEqual(A, solution(5), "Should return a spiral array with corresponding input")
