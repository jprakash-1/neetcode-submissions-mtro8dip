class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, num in enumerate(nums): 
            if num > 0: 
                break 

            if index > 0 and num == nums[index - 1]: 
                continue

            left = index + 1 
            right = len(nums) - 1 

            while(left < right): 
                if num + nums[left] + nums[right] == 0: 
                    result.append([num, nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right: 
                        left += 1

                elif num + nums[left] + nums[right] > 0:
                    right -= 1 
                elif num + nums[left] + nums[right] < 0:
                    left += 1 
        
        return result
        # return set(result)
