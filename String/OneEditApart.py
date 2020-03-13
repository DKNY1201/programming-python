import unittest


def one_edit_apart(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    has_wrong_char = False

    # make sure s1 always longer than or equal s2
    if len(s1) < len(s2):
        temp = s1
        s1 = s2
        s2 = temp

    i, j = 0, 0

    while j < len(s2):
        if s1[i] != s2[j]:
            if has_wrong_char:
                return False

            has_wrong_char = True

            if len(s1) > len(s2):
                i += 1

        i += 1
        j += 1

    return True


class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(False, one_edit_apart("cat", "dog"), "Should return False if can not transform first string to"
                                                            " second string in one edit")
        self.assertEqual(True, one_edit_apart("cat", "cats"), "Should return True if can not transform first string to"
                                                            " second string in one edit")
        self.assertEqual(True, one_edit_apart("cat", "cut"), "Should return True if can not transform first string to"
                                                            " second string in one edit")
        self.assertEqual(True, one_edit_apart("cat", "cast"), "Should return True if can not transform first string to"
                                                            " second string in one edit")
        self.assertEqual(True, one_edit_apart("cat", "at"), "Should return True if can not transform first string to"
                                                            " second string in one edit")
        self.assertEqual(False, one_edit_apart("cat", "act"), "Should return False if can not transform first string to"
                                                            " second string in one edit")