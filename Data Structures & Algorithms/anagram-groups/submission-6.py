class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            key = [0] * 26

            for char in word:
                key[ord(char) - ord('a')] += 1

            key = tuple(key)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        return list(anagrams.values())