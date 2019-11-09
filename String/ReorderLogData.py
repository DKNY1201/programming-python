import unittest


def reorder_log_files(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    if not logs:
        return logs

    lets = []
    digs = []

    for log in logs:
        idx = log.find(" ")
        if log[idx + 1].isnumeric():
            digs.append(log)
        else:
            lets.append(log)

    tuples = []

    for let in lets:
        idx = let.find(" ")
        tuples.append((let[idx + 1:], let))

    tuples.sort(key=lambda tup: (tup[0], tup[1]))
    result = [tup[1] for tup in tuples]
    result.extend(digs)

    return result


class Test(unittest.TestCase):
    def test_num_islands(self):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        expected = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        self.assertEqual(expected, reorder_log_files(logs), "Should reorder log files correctly")

        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        expected = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        self.assertEqual(expected, reorder_log_files(logs), "Should reorder log files correctly")

        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]
        expected = ["a2 act car", "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        self.assertEqual(expected, reorder_log_files(logs), "Should reorder log files correctly")
