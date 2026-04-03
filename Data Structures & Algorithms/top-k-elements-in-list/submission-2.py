from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        output = [key for key, values in sorted(num_freq.items(), key = lambda x: x[1], reverse=True)]
        return output[:k]
            

