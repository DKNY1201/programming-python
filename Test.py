class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) <= 1:
        #     return s

        maximum = float("-Inf")
        res = ""

        for i in range(len(s)):
            palind1 = self.get_palind(s, i, i)
            palind2 = self.get_palind(s, i, i + 1)

            palind = palind1 if len(palind1) >= len(palind2) else palind2

            # if s itself is a palindromic then return s
            if len(palind) == len(s):
                return s

            if len(palind) > maximum:
                maximum = len(palind)
                res = palind

        return res

    def get_palind(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i + 1:j]


s = Solution()

print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("babbbbac"))
print(s.longestPalindrome("abccbadcakz"))
print(s.longestPalindrome("a"))