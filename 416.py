# 给你一个
# 只包含正整数
# 的
# 非空
# 数组
# nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#
#
# 示例
# 1：
#
# 输入：nums = [1, 5, 11, 5]
# 输出：true
# 解释：数组可以分割成[1, 5, 5]
# 和[11] 。
# 示例
# 2：
#
# 输入：nums = [1, 2, 3, 5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

# 测试 main 函数
if __name__ == "__main__":
    sol = Solution()

    # 测试样例
    test_cases = [
        ([1, 5, 11, 5], True),  # 可以分割成 [1, 5, 5] 和 [11]
        ([1, 2, 3, 5], False),  # 不能分割
        ([2, 2, 1, 1], True),  # 可以分割成 [2, 1] 和 [2, 1]
        ([1, 2, 5], False),  # 不能分割
    ]

    for nums, expected in test_cases:
        result = sol.canPartition(nums)
        print(f"Input: {nums} -> Output: {result} | Expected: {expected}")
