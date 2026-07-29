class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1) 
        word2_len = len(word2)
        word_len = min(word1_len, word2_len)
        output = ""
        for i in range(word_len): 
            output += word1[i] + word2[i]
        if word_len == word1_len: 
            output += word2[word_len:]
        else: 
            output += word1[word_len:]
        return output