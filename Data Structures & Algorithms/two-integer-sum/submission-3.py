from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {}
        for index,num in enumerate(nums): 
            num2 = target - num 
            if num2 in value_dict: 
                return [value_dict[num2], index]
            else: 
                value_dict[num] = index

        return []