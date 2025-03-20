class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)

        def dfs(val, index):
            nonlocal res
            if index == length:
                res += val
                return
            dfs(val, index + 1)
            dfs(val ^ nums[index], index + 1)

        dfs(0, 0)
        return res
