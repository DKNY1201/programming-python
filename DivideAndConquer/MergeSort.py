import unittest


def merge_sort_res(nums):
    if len(nums) <= 1:
        return nums

    pivot = len(nums) // 2
    left_nums = merge_sort_res(nums[0:pivot])
    right_nums = merge_sort_res(nums[pivot:])

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


def merge_sort_iter(nums):
    if len(nums) <= 1:
        return nums

    res = []

    for num in nums:
        res.append([num])

    i = 0
    j = 0

    while len(res) > 1:
        while i < len(res):
            sorted_chunk = res[i] if i + 1 >= len(res) else merge(res[i], res[i + 1])
            res[j] = sorted_chunk
            i += 2
            j += 1

        res = res[0:j]
        i = 0
        j = 0

    return res[0]

class TestMergeSort(unittest.TestCase):

    def test_normal_recursive(self):
        self.assertEqual(merge_sort_res([9, 4, 7, 6, 1, 5, 3, 2]), [1, 2, 3, 4, 5, 6, 7, 9],
                         "Recursive - Should sort list ascending order")

    def test_empty_recursive(self):
        self.assertEqual(merge_sort_res([]), [],
                         "Recursive - Should return empty list if input is empty list")

    def test_sorted_ascending_recursive(self):
        self.assertEqual(merge_sort_res([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Recursive - Should return correct result for ascending sorted list")

    def test_sorted_descending_recursive(self):
        self.assertEqual(merge_sort_res([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Recursive - Should return correct result for descending sorted list")

    def test_duplicate_recursive(self):
        self.assertEqual(merge_sort_res([9, 4, 7, 6, 1, 5, 3, 2, 1, 9]), [1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Recursive - Should return correct result if input has duplicate nums")

    def test_negative_recursive(self):
        self.assertEqual(merge_sort_res([9, 4, 7, 6, 1, 5, 3, 2, -1, 9, -3, -100]),
                         [-100, -3, -1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Recursive - Should return correct result if input has negative nums")

    def test_normal_iter(self):
        self.assertEqual(merge_sort_iter([9, 4, 7, 6, 1, 5, 3, 2]), [1, 2, 3, 4, 5, 6, 7, 9],
                         "Iteration - Should sort list ascending order")

    def test_empty_iter(self):
        self.assertEqual(merge_sort_iter([]), [],
                         "Should return empty list if input is empty list")

    def test_sorted_ascending_iter(self):
        self.assertEqual(merge_sort_iter([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should return correct result for ascending sorted list")

    def test_sorted_descending_iter(self):
        self.assertEqual(merge_sort_iter([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9],
                         "Should return correct result for descending sorted list")

    def test_duplicate_iter(self):
        self.assertEqual(merge_sort_iter([9, 4, 7, 6, 1, 5, 3, 2, 1, 9]), [1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should return correct result if input has duplicate nums")

    def test_negative_iter(self):
        self.assertEqual(merge_sort_iter([9, 4, 7, 6, 1, 5, 3, 2, -1, 9, -3, -100]),
                         [-100, -3, -1, 1, 2, 3, 4, 5, 6, 7, 9, 9],
                         "Should return correct result if input has negative nums")
