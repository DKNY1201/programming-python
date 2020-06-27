import unittest


def precise_bin_search(nums, k):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2

        if nums[m] < k:
            l = m + 1
        else:
            r = m - 1

    return nums[l] == k if 0 <= l < len(nums) else False


class Test(unittest.TestCase):
    def test(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 10
        self.assertEqual(True, precise_bin_search(nums, k), "Should return True if number to search is in nums")

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 11
        self.assertEqual(False, precise_bin_search(nums, k), "Should return False if number to search is not in nums")

        nums = []
        for i in range(10**7):
            nums.append(i)
        k = 8567412
        self.assertEqual(True, precise_bin_search(nums, k), "Should return True if number to search is in nums")
