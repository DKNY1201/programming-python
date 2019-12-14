"""
https://leetcode.com/problems/prison-cells-after-n-days/
"""

import unittest


def prison_cells_after_n_days(cells, n):
    seen = dict()

    while n > 0:
        seen[str(cells)] = n
        n -= 1
        next_cells = next_day_prison(cells)

        if str(next_cells) in seen:
            n %= seen[str(next_cells)] - n

        cells = next_cells[:]

    return cells


def next_day_prison(cells):
    next_cells = [0] * 8

    for i in range(1, 7):
        next_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0

    return next_cells


class Test(unittest.TestCase):
    def test_prison_cells_after_n_days(self):
        # cells = [0, 1, 0, 1, 1, 0, 0, 1]
        # N = 0
        # self.assertEqual(cells, prison_cells_after_n_days(cells, N),
        #                  "Should return first initial cells if N is 0")
        #
        # cells = [0, 1, 0, 1, 1, 0, 0, 1]
        # N = 7
        # self.assertEqual([0, 0, 1, 1, 0, 0, 0, 0], prison_cells_after_n_days(cells, N),
        #                  "Should return correct state of prison after N days")

        cells = [1, 0, 0, 1, 0, 0, 1, 0]
        N = 1000000000
        self.assertEqual([0, 0, 1, 1, 1, 1, 1, 0], prison_cells_after_n_days(cells, N),
                         "Should return correct state of prison after N days")
