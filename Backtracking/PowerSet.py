def power_set(s):
    ps = []
    helper(s, ps, 0, "")

    return ps


def helper(s, ps, i, subset):
    if i == len(s):
        ps.append(subset)
        return

    helper(s, ps, i+1, subset)
    helper(s, ps, i+1, subset + s[i])


print(power_set("abc"))
print(power_set("abcd"))