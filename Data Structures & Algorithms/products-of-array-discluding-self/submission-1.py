class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = []

        prefix = 1 
        for index, num in enumerate(nums): 
            prefix_mul.append(prefix)
            prefix *= num 

        
        postfix = 1 
        postfix_mul = [1]*(len(nums) )
        for index in range(len(nums) - 1, -1, -1): 
            postfix_mul[index] = postfix * prefix_mul[index]
            postfix *= nums[index]

        return postfix_mul