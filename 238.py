# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
#
# 提示：
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# 输入 保证 数组 answer[i] 在  32 位 整数范围内
#
#
    # 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(n)):

            answer[i] = R * answer[i]
            R *= nums[i]

        return answer




def test_product_except_self():
    solution = Solution()

    # 测试用例 1
    nums1 = [1, 2, 3, 4]
    expected1 = [24, 12, 8, 6]
    assert solution.productExceptSelf(
        nums1) == expected1, f"Test 1 Failed: expected {expected1}, got {solution.productExceptSelf(nums1)}"

    # 测试用例 2
    nums2 = [-1, 1, 0, -3, 3]
    expected2 = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(
        nums2) == expected2, f"Test 2 Failed: expected {expected2}, got {solution.productExceptSelf(nums2)}"

    # 边界测试：全部是1
    nums3 = [1, 1, 1, 1]
    expected3 = [1, 1, 1, 1]
    assert solution.productExceptSelf(
        nums3) == expected3, f"Test 3 Failed: expected {expected3}, got {solution.productExceptSelf(nums3)}"

    # 边界测试：只有两个元素
    nums4 = [2, 3]
    expected4 = [3, 2]
    assert solution.productExceptSelf(
        nums4) == expected4, f"Test 4 Failed: expected {expected4}, got {solution.productExceptSelf(nums4)}"

    # 边界测试：包含多个0
    nums5 = [0, 0]
    expected5 = [0, 0]
    assert solution.productExceptSelf(
        nums5) == expected5, f"Test 5 Failed: expected {expected5}, got {solution.productExceptSelf(nums5)}"

    print("All tests passed.")


if __name__ == "__main__":
    # 调用测试函数
    test_product_except_self()