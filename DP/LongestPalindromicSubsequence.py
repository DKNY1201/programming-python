import unittest


class Solution:
    m = float("-Inf")

    def longestPalindromeSubseq(self, s: str) -> int:
        self.helper(s, 0, "")

        return self.m

    def helper(self, s, i, prefix):
        if i > len(s):
            return

        if self.is_palind(prefix):
            self.m = max(self.m, len(prefix))
            print(prefix)

        if i < len(s):
            self.helper(s, i + 1, prefix)
            self.helper(s, i + 1, prefix + s[i])

    def is_palind(self, s):
        if not s:
            return False

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


s = Solution()

print(s.longestPalindromeSubseq("bbbab"))
print("===")
print(s.longestPalindromeSubseq("abbcda"))
print("===")
print(s.longestPalindromeSubseq("abbcdabckdsab"))
print("===")
print(s.longestPalindromeSubseq("aaaaaaaaaaaaaaaaaaaaa"))
