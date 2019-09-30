import unittest


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = len(nums) // 2
    left_nums = merge_sort(nums[0:pivot])
    right_nums = merge_sort(nums[pivot:])

    return merge(left_nums, right_nums)


def merge(left_nums, right_nums):
    if len(left_nums) == 0:
        return right_nums
    if len(right_nums) == 0:
        return left_nums

    i = 0
    j = 0
    res = []

    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] < right_nums[j]:
            res.append(left_nums[i])
            i += 1
        else:
            res.append(right_nums[j])
            j += 1

    res.extend(left_nums[i:])
    res.extend(right_nums[j:])

    return res


class TestStringMethods(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(merge_sort([9, 4, 7, 6, 1, 5, 3, 2]), [1, 2, 3, 4, 5, 6, 7, 9],
                         "Should sort list ascending order")

    def test_empty(self):
        self.assertEqual(merge_sort([]), [],
                         "Should return empty list if input is empty list")

    def test_sorted_ascending(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should return correct result for ascending sorted list")

    def test_sorted_descending(self):
        self.assertEqual(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should return correct result for descending sorted list")

    def test_duplicate(self):
        self.assertEqual(merge_sort([9, 4, 7, 6, 1, 5, 3, 2, 1, 9]), [1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should return correct result if input has duplicate nums")

    def test_negative(self):
        self.assertEqual(merge_sort([9, 4, 7, 6, 1, 5, 3, 2, -1, 9, -3, -100]),
                         [-100, -3, -1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should return correct result if input has negative nums")
