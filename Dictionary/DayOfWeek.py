"""
https://leetcode.com/discuss/interview-question/398047/
"""
import unittest


def solution(s, k):
    week_to_num = {
        "Mon": 0,
        "Tue": 1,
        "Web": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }

    num_to_week = {
        0: "Mon",
        1: "Tue",
        2: "Web",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
    }

    return num_to_week[(week_to_num[s] + k) % 7]


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual("Fri", solution("Web", 2), "Should return correct day after k days of given day")
        self.assertEqual("Mon", solution("Sat", 23), "Should return correct day after k days of given day")
        self.assertEqual("Sat", solution("Sat", 0), "Should return correct day after k days of given day")
        self.assertEqual("Fri", solution("Tue", 500), "Should return correct day after k days of given day")