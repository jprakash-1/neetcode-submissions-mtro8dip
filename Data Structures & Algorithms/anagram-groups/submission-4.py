from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_words = {}
        for word in strs: 
            word_dict = Counter(word)
            key = tuple(sorted(word_dict.items()))
            grouped_words[key] = grouped_words.get(key,[]) + [word]

        return list(grouped_words.values())