class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}

        for index, num in enumerate(nums): 
            if target - num in num2index: 
                return [num2index[target - num], index]
            else: 
                num2index[num] = index 
