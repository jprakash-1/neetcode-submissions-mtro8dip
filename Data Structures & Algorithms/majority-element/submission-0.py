class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element, count = 0, 0 

        for num in nums: 
            if count == 0: 
                majority_element = num 

            count += (1 if num == majority_element else -1)
        return majority_element