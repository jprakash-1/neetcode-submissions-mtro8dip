from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        s1_freq = Counter(s1)
        s2_freq = Counter()
        start = 0

        for end in range(n):
            # add current char
            s2_freq[s2[end]] += 1

            # shrink if window too large
            if end - start + 1 > m:
                left_char = s2[start]
                s2_freq[left_char] -= 1
                if s2_freq[left_char] == 0:
                    del s2_freq[left_char]
                start += 1

            # compare only when window size == m
            if end - start + 1 == m and s2_freq == s1_freq:
                return True

        return False
