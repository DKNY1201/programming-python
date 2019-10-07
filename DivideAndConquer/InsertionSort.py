import unittest


def insertion_sort(nums):
    if len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
            else:
                break


def binary_insertion_sort(nums):
    if len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):
        l = 0
        r = i - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[i]:
                if m == 0 or nums[m - 1] <= nums[i]:
                    shift_right(nums, m, i - 1)
                    break

                r = m - 1
            else:
                if nums[m + 1] > nums[i]:
                    shift_right(nums, m + 1, i - 1)

                l = m + 1


def shift_right(nums, s, e):
    for i in range(e, s - 1, -1):
        nums[i + 1], nums[i] = nums[i], nums[i + 1]


class Test(unittest.TestCase):

    def test_normal(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2, 5, 1, 7, 0, 9]
        insertion_sort(nums)
        self.assertEqual(nums, [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9], "Should sort list ascending order")

    def test_empty(self):
        nums = []
        insertion_sort(nums)
        self.assertEqual(nums, [], "Should return empty list if input is empty list")

    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should return correct result for ascending sorted list")

    def test_sorted_descending(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should return correct result for descending sorted list")

    def test_binary_normal(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2, 5, 1, 7, 0, 9]
        binary_insertion_sort(nums)
        self.assertEqual(nums, [0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9], "Should sort list ascending order")

    def test_binary_empty(self):
        nums = []
        binary_insertion_sort(nums)
        self.assertEqual(nums, [], "Should return empty list if input is empty list")

    def test_binary_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        binary_insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should return correct result for ascending sorted list")

    def test_binary_sorted_descending(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        binary_insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should return correct result for descending sorted list")