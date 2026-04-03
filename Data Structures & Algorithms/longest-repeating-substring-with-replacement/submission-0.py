class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        maxfreq = 0 
        hash_map = {}
        max_len = 0

        for right in range(len(s)): 
            hash_map[s[right]] = hash_map.get(s[right],0) + 1 

            maxfreq = max(maxfreq, hash_map[s[right]])
            
            while (right - left + 1) - maxfreq > k:
                hash_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)


        return max_len
            


            