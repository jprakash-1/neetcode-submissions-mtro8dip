class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        final_ans = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = N - 1
            while (j < k): 
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    triplet = tuple(triplet)
                    final_ans.add(triplet)
                    j += 1
                    k -= 1
                
                elif nums[i] + nums[j] + nums[k] > 0: 
                    k -= 1

                elif nums[i] + nums[j] + nums[k] < 0: 
                    j += 1
        return list(final_ans)