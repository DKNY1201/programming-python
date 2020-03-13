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