"""
https://leetcode.com/discuss/interview-question/398031/
"""
import unittest


def solution(s):
    """
    Using sliding window technique to solve this problem.
    Whenever we have 3 same consecutive letters then we extract string and assign to the result if it's longer than the
    result and move left pointer to letter right before current pointer to start new check.
    """
    l, r, count = 0, 1, 1
    res = ""

    while r < len(s):
        if s[r] == s[r - 1]:
            count += 1

            if count > 2:
                count = 2
                res = s[l:r] if (r - l) > len(res) else res
                l = r - 1
        else:
            count = 1

        r += 1

    return s[l:r] if (r - l) > len(res) else res


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual("aabbaa", solution("aabbaaaaabb"),
                         "Should return longest sub string without 3 contiguous occurrences of letter")

        self.assertEqual("aabbaabbaabbaa", solution("aabbaabbaabbaa"),
                         "Should return longest sub string without 3 contiguous occurrences of letter")

        self.assertEqual("aabbaabbaa", solution("aabbbaaabbaabbaaa"),
                         "Should return longest sub string without 3 contiguous occurrences of letter")

        self.assertEqual("abbaabbaa", solution("abbaabbaaabbaaa"),
                         "Should return longest sub string without 3 contiguous occurrences of letter")