"""
https://leetcode.com/discuss/interview-question/365872/
"""
import unittest


def numbers_with_equal_digit_sum(A):
    d = dict()
    res = -1

    for n in A:
        digits_sum = calc_digits_sum(n)

        if digits_sum in d:
            max_sum_so_far = d[digits_sum]
            res = max(res, max_sum_so_far + n)
            # update max sum so far
            d[digits_sum] = max(d[digits_sum], n)
        else:
            d[digits_sum] = n

    return res


def calc_digits_sum(n):
    sum = 0

    while n != 0:
        sum += n % 10
        n //= 10

    return sum


def calc_max1_max2_sum(A):
    if len(A) < 2:
        return -1

    max1 = float("-Inf")
    max2 = float("-Inf")

    for n in A:
        if n > max1:
            max2 = max1
            max1 = n
        else:
            if n > max2:
                max2 = n

    return max1 + max2


class Test(unittest.TestCase):

    def test_normal(self):
        A = [51, 71, 17, 42]
        self.assertEqual(93, numbers_with_equal_digit_sum(A), "Should return max of pair that have equal digit sum")

    def test_normal(self):
        A = [42, 33, 60]
        self.assertEqual(102, numbers_with_equal_digit_sum(A), "Should return max of pair that have equal digit sum")

    def test_empty(self):
        A = []
        self.assertEqual(-1, numbers_with_equal_digit_sum(A), "Should return -1 if given array is empty")

    def test_no_equal_digit_pair(self):
        A = [12, 23, 45]
        self.assertEqual(-1, numbers_with_equal_digit_sum(A), "Should return -1 if there is no equal digit pair")