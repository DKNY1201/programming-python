import unittest


def max_heapify(nums, i):
    l = 2 * i
    r = 2 * i + 1

    # we are using 1 index so need to reduce 1 to get correct value
    i -= 1
    l -= 1
    r -= 1
    lg = i

    if l < len(nums) and nums[l] > nums[i]:
        lg = l
    if r < len(nums) and nums[r] > nums[lg]:
        lg = r

    if lg != i:
        nums[i], nums[lg] = nums[lg], nums[i]
        # +1 for 1 index
        max_heapify(nums, lg + 1)


def build_max_heap(nums):
    for i in range(len(nums) // 2, 0, -1):
        max_heapify(nums, i)


def heap_sort(nums):
    # build max heap from nums
    # get max from 1st element => put it to result
    # swap max with last element
    # reduce heap size
    # max_heapify(nums, 1)
    # repeat step 2 -> end until nums is empty
    if len(nums) <= 1:
        return nums

    res = []
    build_max_heap(nums)

    while nums:
        res.append(nums[0])
        nums[0], nums[len(nums) - 1] = nums[len(nums) - 1], nums[0]
        del nums[-1]
        max_heapify(nums, 1)

    return res


class Test(unittest.TestCase):
    def test_normal(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2, 5, 1, 7, 0, 9]
        self.assertEqual(heap_sort(nums), [9, 9, 7, 7, 6, 5, 5, 4, 3, 2, 1, 1, 0], "Should sort list descending order")

    def test_empty(self):
        nums = []
        self.assertEqual(heap_sort(nums), [], "Should return empty list if input is empty list")

    def test_sorted_ascending(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(heap_sort(nums), [9, 8, 7, 6, 5, 4, 3, 2, 1],
                         "Should return correct result for ascending sorted list")

    def test_sorted_descending(self):
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(heap_sort(nums), [9, 8, 7, 6, 5, 4, 3, 2, 1],
                         "Should return correct result for descending sorted list")
