class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = num + nums[left] + nums[right]

                if total == 0:
                    result.append((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(x) for x in set(result)]