from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = {}
        for word in strs: 
            char_freq = [0]*26 
            for char in word: 
                char_freq[ord(char) - ord('a')] += 1 

            key = tuple(char_freq)
            grouped_words[key] = grouped_words.get(key,[]) + [word]
        return list(grouped_words.values())
