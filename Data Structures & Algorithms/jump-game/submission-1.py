class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) 
        goal = n - 1

        for index in range(n-2, -1,-1): 
            if nums[index] + index >= goal: 
                goal = index 

        return goal == 0