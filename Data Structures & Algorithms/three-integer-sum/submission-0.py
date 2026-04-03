class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        final_ans = set()
        for i in range(len(nums)):
            for j in range(i+1,N):
                for k in range(j+1,N): 
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        triplet = tuple(triplet)
                        final_ans.add(triplet)
        
        return list(final_ans)