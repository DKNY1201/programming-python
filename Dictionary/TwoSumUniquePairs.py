"""
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
"""
import unittest


def two_sum_unique_pairs(nums, target):
    # keep track first number of pair
    set1 = set()
    # keep track second number of pair
    set2 = set()
    res = 0

    for n in nums:
        set1.add(n)

    for n in set1:
        num_to_check = target - n

        # to prevent examine n which was num_to_check
        if num_to_check in set1 and n not in set2:
            res += 1
            set2.add(num_to_check)

    return res


class Test(unittest.TestCase):
    def test_two_sum_unique_pairs(self):
        nums = [1, 1, 2, 45, 46, 46]
        target = 47
        self.assertEqual(2, two_sum_unique_pairs(nums, target),
                         "Should return number of unique pairs that add up to target")

        nums = [1, 1]
        target = 2
        self.assertEqual(1, two_sum_unique_pairs(nums, target),
                         "Should return number of unique pairs that add up to target")

        nums = [1, 5, 1, 5]
        target = 6
        self.assertEqual(1, two_sum_unique_pairs(nums, target),
                         "Should return number of unique pairs that add up to target")

        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        target = 2
        self.assertEqual(1, two_sum_unique_pairs(nums, target),
                         "Should return number of unique pairs that add up to target")

        nums = [0, 0, -2, 2, -1, 1, 5, -5, 10, -10, 0, -2, 2, 5, 10, -5]
        target = 0
        self.assertEqual(5, two_sum_unique_pairs(nums, target),
                         "Should return number of unique pairs that add up to target")