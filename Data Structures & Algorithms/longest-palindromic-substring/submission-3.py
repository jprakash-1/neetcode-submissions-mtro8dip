class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                if s[l:r+1] == s[l:r+1][::-1]:
                    if r - l + 1 > len(res):
                        res = s[l:r+1]

        return res