import unittest


def solution(n):
    if not n:
        return ""

    val = "1"

    for i in range(n):
        print(val)
        val = get_next_val(val)


def get_next_val(s):
    count = 1
    l = len(s)
    res = ""

    for i in range(1, l + 1):
        if i == l or s[i] != s[i - 1]:
            res += str(count) + str(s[i - 1])
            count = 1
        else:
            count += 1

    return res


solution(10)
#
# class Test(unittest.TestCase):
#     def test_solution(self):
#         self.assertEqual("1", solution(1), "Should return a correct look and say output for given input")
#         self.assertEqual("11", solution(2), "Should return a correct look and say output for given input")
#         self.assertEqual("21", solution(3), "Should return a correct look and say output for given input")
#         self.assertEqual("1211", solution(4), "Should return a correct look and say output for given input")
#         self.assertEqual("111221", solution(5), "Should return a correct look and say output for given input")
#         self.assertEqual("312211", solution(6), "Should return a correct look and say output for given input")
#         self.assertEqual("13112221", solution(7), "Should return a correct look and say output for given input")
#         self.assertEqual("1113213211", solution(8), "Should return a correct look and say output for given input")
#         self.assertEqual("31131211131221", solution(9), "Should return a correct look and say output for given input")
#         self.assertEqual("13211311123113112211", solution(10),
#                          "Should return a correct look and say output for given input")
