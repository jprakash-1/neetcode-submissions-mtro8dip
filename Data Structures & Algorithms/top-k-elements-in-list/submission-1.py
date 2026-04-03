from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        output = []
        num_freq_sorted = sorted(num_freq.items(), key = lambda x: x[1], reverse = True)
        output = [num for num, _ in num_freq_sorted[:k]]
        
        return output