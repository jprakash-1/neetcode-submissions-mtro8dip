class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        shortest_str = min(strs)
        index = 0
        for char in strs[0]: 
            print(char)
            for word in strs: 
                # print(index, word[index], word)
                if index < len(word) and word[index] == char  : 
                    continue 
                else: 
                    return common_prefix 
            common_prefix += char
            index+= 1 
        return common_prefix