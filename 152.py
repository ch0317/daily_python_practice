# 给你一个整数数组
# nums ，请你找出数组中乘积最大的非空连续
# 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个
# 32 - 位
# 整数。
#
#
#
# 示例
# 1:
#
# 输入: nums = [2, 3, -2, 4]
# 输出: 6
# 解释: 子数组[2, 3]
# 有最大乘积
# 6。
# 示例
# 2:
#
# 输入: nums = [-2, 0, -1]
# 输出: 0
# 解释: 结果不能为
# 2, 因为[-2, -1]
# 不是子数组。

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            temp_max = max(nums[i], max_product*nums[i], min_product*nums[i])
            min_product = min(nums[i], nums[i] * min_product, nums[i] * max_product)
            max_product = temp_max
            result = max(result, max_product)

        return result

if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    sol = Solution()
    print(sol.maxProduct(nums))  # 输出: 6

    nums = [-4,-3,-2]
    sol = Solution()
    print(sol.maxProduct(nums))  # 输出: 12
