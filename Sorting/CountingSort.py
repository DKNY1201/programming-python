import unittest


def counting_sort(A):
    max = get_max(A)
    min = get_min(A)
    has_neg = False

    if min < 0:
        has_neg = True
        # adjust A to prevent neg index in L
        for i, _ in enumerate(A):
            A[i] += -min

    # need to adjust size of L to prevent out of index
    L = [0] * ((max + -min if has_neg else max) + 1)

    for num in A:
        L[num] += 1

    i = 0
    for idx, repeatTimes in enumerate(L):
        for j in range(repeatTimes):
            A[i] = idx
            i += 1

    if has_neg:
        # restore correct value for A
        for i, _ in enumerate(A):
            A[i] -= -min


def get_max(A):
    if not A:
        # should throw exception instead
        return -1

    max = A[0]

    for num in A:
        if num > max:
            max = num

    return max


def get_min(A):
    if not A:
        # should throw exception instead
        return -1

    min = A[0]

    for num in A:
        if num < min:
            min = num

    return min


class TestMergeSort(unittest.TestCase):
    def test_get_max(self):
        nums = [-10, 3, 100, 999, 5, 0]
        self.assertEqual(get_max(nums), 999, "Should return correct maximum number in list")

    def test_get_min(self):
        nums = [-10, 3, 100, 999, 5, 0]
        self.assertEqual(get_min(nums), -10, "Should return correct minimum number in list")

    def test_count_sort(self):
        nums = [9, 4, 7, 6, 1, 5, 3, 2]
        counting_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 9], "Should sort list ascending order")

        nums = []
        counting_sort(nums)
        self.assertEqual(nums, [], "Should sort correctly for empty list")

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        counting_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should sort correctly for ascending sorted list")

        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        counting_sort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Should sort correctly for descending sorted list")

        nums = [9, 4, 7, 6, 1, 5, 3, 2, 1, 9]
        counting_sort(nums)
        self.assertEqual(nums, [1, 1, 2, 3, 4, 5, 6, 7, 9, 9], "Should sort correctly for duplicated list")

        nums = [9, 4, 7, 6, 1, 5, 3, 2, -1, 9, -3, -100]
        counting_sort(nums)
        self.assertEqual(nums, [-100, -3, -1, 1, 2, 3, 4, 5, 6, 7, 9, 9], "Should sort correctly for duplicated-negatived list")
