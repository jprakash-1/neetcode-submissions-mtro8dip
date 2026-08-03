class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_prefix = 1 
        prefix = []
        for i in range(0, len(nums)): 
            prefix.append(curr_prefix)
            curr_prefix *= nums[i]

        print(prefix)
        curr_postfix = 1 
        postfix = []
        for i in range(len(nums) - 1, -1, -1): 
            postfix.append(curr_postfix*prefix[i])
            curr_postfix *= nums[i]

        
        return postfix[::-1]