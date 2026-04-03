class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        index = 0
        min_len = min([len(word) for word in strs])
        print(min_len)
        while(index < min_len): 
            char = strs[0][index]
            for word in strs: 
                if char != word[index]: 
                    return common_prefix
            common_prefix += char 
            index += 1 
        return common_prefix

            