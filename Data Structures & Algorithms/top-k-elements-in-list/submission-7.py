from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        # output = [key for key, values in sorted(num_freq.items(), key = lambda x: x[1], reverse=True)]
         
        output = heapq.nlargest(k, num_freq.keys(), key= num_freq.get)
        return output
        
        
        
            

