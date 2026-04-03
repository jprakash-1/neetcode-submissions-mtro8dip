class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = set()
        max_len = 0

        for end in range(len(s)):
            while s[end] in seen:          # <-- change 1: if -> while
                seen.remove(s[start])
                start += 1

            seen.add(s[end])
            max_len = max(max_len, end - start + 1)

        return max_len
