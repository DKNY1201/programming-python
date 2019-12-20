"""
Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same. There can be at max A 'a', B 'b' and C 'c'.

Example 1:

Input: A = 1, B = 1, C = 6
Output: "ccbccacc"
Example 2:

Input: A = 1, B = 2, C = 3
Output: "acbcbc"
"""
import unittest


def longest_string_without_3_consecutive_chars(A, B, C):
    input = [0] * 3
    input[0], input[1], input[2] = A, B, C
    map = {0: "a", 1: "b", 2: "c"}
    max_idx, sec_max_idx = get_max_sec_max_idx(input)
    res = ""

    while input[max_idx] and input[sec_max_idx] > 0:
        if input[max_idx] // input[sec_max_idx] >= 2:
            res += map[max_idx] * 2 + map[sec_max_idx]
            input[max_idx] -= 2
            input[sec_max_idx] -= 1
        else:
            if input[max_idx] >= 2:
                res += map[max_idx] * 2
                input[max_idx] -= 2
            else:
                res += map[max_idx] * 1
                input[max_idx] -= 1

            if input[sec_max_idx] >= 2:
                res += map[sec_max_idx] * 2
                input[sec_max_idx] -= 2
            else:
                res += map[sec_max_idx] * 1
                input[sec_max_idx] -= 1

        max_idx, sec_max_idx = get_max_sec_max_idx(input)

    res += map[max_idx] * 2 if input[max_idx] >= 2 else map[max_idx] if input[max_idx] > 0 else ""

    return res


def get_max_sec_max_idx(input):
    max_idx = 0
    sec_max_idx = 0
    maxx = -1
    sec_max = -1

    for i, n in enumerate(input):
        if n > maxx:
            sec_max = maxx
            sec_max_idx = max_idx
            maxx = n
            max_idx = i
        elif n > sec_max:
            sec_max = n
            sec_max_idx = i

    return max_idx, sec_max_idx


class Test(unittest.TestCase):
    def test_longest_string_without_3_consecutive_chars(self):
        self.assertEqual("ccaccbcc", longest_string_without_3_consecutive_chars(1, 1, 6),
                         "Should return longest string without 3 consecutive characters")

        self.assertEqual("ccbbac", longest_string_without_3_consecutive_chars(1, 2, 3),
                         "Should return longest string without 3 consecutive characters")

        self.assertEqual("aabbaabbaabbaabaaccaabbaaccb", longest_string_without_3_consecutive_chars(14, 10, 4),
                         "Should return longest string without 3 consecutive characters")

        self.assertEqual("aabaabaacaabaacaabaac", longest_string_without_3_consecutive_chars(14, 4, 3),
                         "Should return longest string without 3 consecutive characters")

    def test_get_max_idx(self):
        self.assertEqual((2, 0), get_max_sec_max_idx([1, 1, 6]), "Should return max and second max index correctly")
        self.assertEqual((1, 0), get_max_sec_max_idx([2, 3, 2]), "Should return max and second max index correctly")
        self.assertEqual((0, 2), get_max_sec_max_idx([5, 2, 4]), "Should return max and second max index correctly")
        self.assertEqual((1, 2), get_max_sec_max_idx([3, 4, 4]), "Should return max and second max index correctly")