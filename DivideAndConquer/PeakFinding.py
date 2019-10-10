import unittest


def peak_finding_1d(nums):
    if len(nums) == 1:
        return nums[0]

    l = 0
    r = len(nums) - 1

    while l < r:
        m = (l + r) // 2

        if nums[m] < nums[m + 1]:
            l = m + 1
        elif nums[m] < nums[m - 1]:
            r = m - 1
        else:
            return nums[m]

    return nums[l]


def peak_finding_2d(grid):
    l = 0
    r = len(grid[0]) - 1

    while l < r:
        m = (l + r) // 2
        max_row_idx = find_max_row_idx(grid, m)

        if grid[max_row_idx][m] < grid[max_row_idx][m + 1]:
            l = m + 1
        elif grid[max_row_idx][m] < grid[max_row_idx][m - 1]:
            r = m - 1
        else:
            return grid[max_row_idx][m]

    max_row_idx = find_max_row_idx(grid, l)

    return grid[max_row_idx][l]


def find_max_row_idx(grid, col):
    max = grid[0][col]
    max_idx = 0

    for i in range(1, len(grid)):
        if grid[i][col] > max:
            max = grid[i][col]
            max_idx = i

    return max_idx


class Test(unittest.TestCase):

    def test_normal_1d(self):
        self.assertIn(peak_finding_1d([9, 4, 7, 6, 1, 5, 3, 2]), [9, 7, 5], "Should return a correct peak")

    def test_ascending_1d(self):
        self.assertEqual(peak_finding_1d([1, 2, 3, 4, 5, 6]), 6,
                         "Should return a correct peak for ascending order list")

    def test_descending_1d(self):
        self.assertEqual(peak_finding_1d([6, 5, 4, 3, 2, 1]), 6,
                         "Should return a correct peak for descending order list")

    def test_one_item_1d(self):
        self.assertEqual(peak_finding_1d([10]), 10, "Should return a correct peak list has only 1 item")

    def test_two_item_1d(self):
        self.assertEqual(peak_finding_1d([10, 9]), 10,
                         "Should return a correct peak list has 2 items and peak is on most left")

    def test_normal_2d(self):
        grid = [
            [2, 6, 7, 5, 100, 50, 2, 4],
            [3, 8, 101, 7, 80, 60, 2, 0],
            [6, 2, 10, 10, 40, 30, 3, 1],
            [5, 10, 40, 60, 41, 4, 2, 6],
            [11, 21, 60, 80, 101, 11, 2, 6],
            [4, 25, 8, 77, 99, 99, 100, 101],
        ]
        self.assertEqual(peak_finding_2d(grid), 101, "Should return a correct peak")

    def test_ascending_2d(self):
        grid = [
            [1],
            [2],
            [5],
            [1],
            [6],
        ]
        self.assertEqual(peak_finding_2d(grid), 6, "Should return a correct peak for grid has only 1 column")

    def test_descending_2d(self):
        grid = [
            [1, 3],
            [2, 6],
            [5, 10],
            [100, 11],
            [6, 101],
        ]
        self.assertEqual(peak_finding_2d(grid), 100, "Should return a correct peak has 2 columns")

    def test_one_item_2d(self):
        grid = [[1, 100, 90, 80, 10, 101]]
        self.assertIn(peak_finding_2d(grid), [100, 101], "Should return a correct peak list has only 1 row")
