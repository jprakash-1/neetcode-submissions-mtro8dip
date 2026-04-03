class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = 0 
        dp = nums
        
        for index in range(1, len(nums)): 
            num = nums[index]
            dp[index] = max(num, dp[index - 1] + num)
            print(dp)
        return max(dp)
