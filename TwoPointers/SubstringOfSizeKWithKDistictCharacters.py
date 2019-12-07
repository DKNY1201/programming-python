"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
"""

import unittest


def get_substrings_of_size_k_with_k_distinct_characters(s, k):
    if not s or not k:
        return []

    # count for number of char stored in checker
    # - increase by 1 if add new char
    # - decrease by 1 if remove a char
    counter = 0
    checker = [0] * 26
    l = len(s)
    res = set()
    # 2 pointers, left and right
    i, j = 0, 0

    while j < l:
        char_idx_j = ord(s[j]) - ord('a')
        checker[char_idx_j] += 1

        if checker[char_idx_j] == 1:
            counter += 1

        # if having k unique chars in window
        if counter == k:
            # shrink size of window to equal k
            while j - i >= k:
                char_idx_i = ord(s[i]) - ord('a')
                checker[char_idx_i] -= 1

                if checker[char_idx_i] == 0:
                    counter -= 1

                i += 1

            # after shrink if still have k unique chars
            if counter == k:
                res.add(s[i:j + 1])

                # move left pointer
                char_idx_i = ord(s[i]) - ord('a')
                checker[char_idx_i] -= 1

                if checker[char_idx_i] == 0:
                    counter -= 1

                i += 1

        j += 1

    res = list(res)
    res.sort()

    return res


class Test(unittest.TestCase):
    def test_normal_recursive(self):
        expected = []
        self.assertEqual(get_substrings_of_size_k_with_k_distinct_characters("", 3), expected,
                         "Should return a correct list of substrings have length k and have k distinct characters")

        expected = []
        self.assertEqual(get_substrings_of_size_k_with_k_distinct_characters("abcabc", 0), expected,
                         "Should return a correct list of substrings have length k and have k distinct characters")

        expected = ["abc", "bca", "cab"]
        expected.sort()
        self.assertEqual(get_substrings_of_size_k_with_k_distinct_characters("abcabc", 3), expected,
                         "Should return a correct list of substrings have length k and have k distinct characters")

        expected = ["bac", "cab"]
        expected.sort()
        self.assertEqual(get_substrings_of_size_k_with_k_distinct_characters("abacab", 3), expected,
                         "Should return a correct list of substrings have length k and have k distinct characters")

        expected = ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
        expected.sort()
        self.assertEqual(get_substrings_of_size_k_with_k_distinct_characters("awaglknagawunagwkwagl", 4), expected,
                         "Should return a correct list of substrings have length k and have k distinct characters")