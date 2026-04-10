class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, remaining):
            if remaining == 0:
                res.append(path.copy())
                return

            if i >= len(nums) or remaining < 0:
                return

            path.append(nums[i])
            dfs(i, remaining - nums[i])   # take nums[i] again
            path.pop()

            dfs(i + 1, remaining)         # skip nums[i]

        dfs(0, target)
        return res