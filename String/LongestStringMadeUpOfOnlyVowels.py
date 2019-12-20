"""
You are given with a string . Your task is to remove atmost two substrings of any length from the given string such that the remaining string contains vowels('a','e','i','o','u') only. Your aim is the maximise the length of the remaining string. Output the length of remaining string after removal of atmost two substrings.
NOTE: The answer may be 0, i.e. removing the entire string.

Sample Input
earthproblem => 3
letsgosomewhere => 2
"""

import unittest


def longest_string_made_up_if_only_vowels(s):
    if not s:
        return 0

    vowels = {"i", "e", "o", "u", "a"}
    l = 0
    r = len(s) - 1
    r_l = 0

    # get len of left boundary vowels
    while s[l] in vowels:
        l += 1

    # get len of right boundary vowels
    while s[r] in vowels:
        r_l += 1
        r -= 1

    # get max len of middle consecutive vowels
    max_consecutive_vowel_len = 0
    cur_consecutive_vowel_len = 0

    for i in range(l, r + 1):
        if s[i] in vowels:
            cur_consecutive_vowel_len += 1
        else:
            max_consecutive_vowel_len = max(cur_consecutive_vowel_len, max_consecutive_vowel_len)
            cur_consecutive_vowel_len = 0

    return l + max_consecutive_vowel_len + r_l


class Test(unittest.TestCase):
    def test_longest_string_made_up_if_only_vowels(self):
        self.assertEqual(0, longest_string_made_up_if_only_vowels(""),
                         "Should return longest string made up of only vowels")

        self.assertEqual(3, longest_string_made_up_if_only_vowels("earthproblem"),
                         "Should return longest string made up of only vowels")

        self.assertEqual(2, longest_string_made_up_if_only_vowels("letsgosomewhere"),
                         "Should return longest string made up of only vowels")

        self.assertEqual(7, longest_string_made_up_if_only_vowels("iaeloveiloveyou"),
                         "Should return longest string made up of only vowels")