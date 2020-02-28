"""
https://leetcode.com/discuss/interview-question/351783/

This solution not return correct minimum swap in some cases. Need to consider move single char to middle or last
"""
import unittest


def min_swap(s):
    if not can_form_palindrome(s):
        return -1

    res = 0
    i = 0
    n = len(s)
    s = list(s)

    while i < n // 2:
        found = False

        for j in range(n - 1 - i, i, -1):
            if s[i] == s[j]:
                found = True

                for k in range(j, n - 1 - i):
                    swap(s, k, k + 1)
                    res += 1

        if not found:
            for k in range(i, n - 1 - i):
                swap(s, k, k + 1)
                res += 1
        else:
            i += 1

    return res


def can_form_palindrome(s):
    map = [0] * 26

    for c in s:
        map[ord(c) - ord('a')] += 1

    has_odd = False

    for count in map:
        if count % 2 == 1:
            if has_odd:
                return False

            has_odd = True

    return True


def swap(s, i, j):
    t = s[i]
    s[i] = s[j]
    s[j] = t


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(3, min_swap("mamad"), "Should return min number of adjacent swap to form palindrome")

        self.assertEqual(-1, min_swap("asflkj"), "Should return -1 if can't form palindrome")

        self.assertEqual(2, min_swap("aabb"), "Should return min number of adjacent swap to form palindrome")

        self.assertEqual(3, min_swap("damam"), "Should return min number of adjacent swap to form palindrome")

        self.assertEqual(1, min_swap("ntiin"), "Should return min number of adjacent swap to form palindrome")