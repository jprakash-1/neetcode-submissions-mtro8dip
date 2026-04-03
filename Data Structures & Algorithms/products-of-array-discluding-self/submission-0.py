class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        
        prefix = 1
        for index ,num in enumerate(nums):
            res[index] *= prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            res[i] *= postfix
            postfix *= num
        return res
