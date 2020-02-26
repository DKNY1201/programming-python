"""
https://leetcode.com/discuss/interview-question/398026/
"""
import unittest


def solution(s):
    res = 0
    n = len(s)
    l = 0

    while l < n - 1:
        r = l + 1
        k = 1

        while r < n:
            if s[l] == s[r]:
                k += 1
                r += 1
            else:
                break

        res += k // 3
        l = r

    return res


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1, solution("baaaaa"),
                         "Should return min number of move to obtain string without 3 consecutive letters")

        self.assertEqual(2, solution("baaabbaabbba"),
                         "Should return min number of move to obtain string without 3 consecutive letters")

        self.assertEqual(0, solution("baabab"),
                         "Should return min number of move to obtain string without 3 consecutive letters")

        self.assertEqual(4, solution("bbbbbbbbbbbbbb"),
                         "Should return min number of move to obtain string without 3 consecutive letters")
