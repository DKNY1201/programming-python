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


class Test(unittest.TestCase):

    def test_normal(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2]
        insertion_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 9], "Should sort list ascending order")

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
