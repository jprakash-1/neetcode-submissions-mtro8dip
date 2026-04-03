class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        final_ans = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            j = i + 1
            k = N - 1
            if i > 0: 
                if nums[i] == nums[i - 1]:
                    continue 
            while (j < k): 
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = ([nums[i], nums[j], nums[k]])
                    final_ans.append(triplet)
                    j += 1
                    k -= 1
                
                    while j < k and nums[j] == nums[j-1]: 
                            j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                            k -= 1
                
                elif nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1

                elif nums[i] + nums[j] + nums[k] < 0: 
                    j += 1


                
        return list(final_ans)