import unittest


def radix_sort(nums, b):
    if not nums or len(nums) <= 1:
        return nums

    min_num = min(nums)

    if min_num < 0:
        # adjust A to always have positive nums
        for idx, _ in enumerate(nums):
            nums[idx] += -min_num

    max_num = max(nums)
    digits = len(str(max_num))

    for d in range(digits):
        L = [[] for i in range(b + 1)]

        for num in nums:
            n = (num // b**d) % b
            L[n].append(num)

        nums = []

        for l in L:
            if l:
                nums.extend(l)

    if min_num < 0:
        # adjust A again to return correct result
        for idx, _ in enumerate(nums):
            nums[idx] -= -min_num

    return nums


class Test(unittest.TestCase):
    def test_radix_sort(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2]
        self.assertEqual(radix_sort(nums, 10), [1, 2, 3, 4, 5, 6, 7, 9], "Should sort list ascending order")

        nums = []
        self.assertEqual(radix_sort(nums, 10), [], "Should sort correctly for empty list")

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(radix_sort(nums, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should sort correctly for ascending sorted list")

        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(radix_sort(nums, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should sort correctly for descending sorted list")

        nums = [9, 4, 7, 6, 1, 5, 3, 2, 1, 9]
        self.assertEqual(radix_sort(nums, 10), [1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should sort correctly for duplicated list")

        nums = [329, 457, 657, 839, 436, 720, 355]
        self.assertEqual(radix_sort(nums, 10), [329, 355, 436, 457, 657, 720, 839],
                         "Should sort correctly for long digits number")

        nums = [329, 57, 657, 839, 6, 720, 1355, 0]
        self.assertEqual(radix_sort(nums, 10), [0, 6, 57, 329, 657, 720, 839, 1355],
                         "Should sort correctly for nums has different length")

        nums = [9, 4, 7, 6, 1, 5, 3, 2, -1, 9, -3, -100]
        self.assertEqual(radix_sort(nums, 10), [-100, -3, -1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should sort correctly for duplicated-negatived list")
