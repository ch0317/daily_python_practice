# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#
#
# 示例 1:
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
# 提示:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 为 无重复元素 的 升序 排列数组
# -104 <= target <= 104
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l

def mytest():
    s = Solution()
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4
    assert s.searchInsert([1,3,5,6], 0) == 0
    print("所有测试通过！")

if __name__ == '__main__':
    mytest()