# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 是一个非递减数组
# -109 <= target <= 109
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)

        left_index = 0

        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        left_index = l

        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1

        right_index = l - 1

        if left_index <= right_index and nums[left_index] == target and nums[right_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))  # [3,4]
    print(s.searchRange([5,7,7,8,8,10], 6))  # [-1,-1]
    print(s.searchRange([], 0))              # [-1,-1]
    print(s.searchRange([1], 1))             # [0,0]
    print(s.searchRange([1,2,3], 2))         # [1,1]
    print(s.searchRange([1,2,2,2,3], 2))     # [1,3]