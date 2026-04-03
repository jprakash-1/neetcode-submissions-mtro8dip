class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_length = float('inf')
        l = 0 
        total = 0

        for index, num in enumerate(nums): 
            total += num
            while total >= target: 
                max_length = min(max_length, index - l + 1)
                total = total - nums[l]
                l += 1 
            

        return 0 if max_length == float("inf") else max_length