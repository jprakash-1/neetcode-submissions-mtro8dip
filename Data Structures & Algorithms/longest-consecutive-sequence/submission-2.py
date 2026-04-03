class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_length = 0
        for num in nums: 
            length = 0
            while num + length in unique_nums: 
                print(num, length)
                length += 1 
                max_length = max(max_length, length)

        return max_length