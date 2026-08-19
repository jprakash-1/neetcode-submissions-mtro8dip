class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for index, num in enumerate(nums): 
            if target - num in vals:
                return [vals[target - num], index]

            vals[num] = index