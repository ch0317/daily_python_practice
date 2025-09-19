# 给你一个整数数组 nums，请你将该数组升序排列。
#
# 你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 解释：数组排序后，某些数字的位置没有改变（例如，2 和 3），而其他数字的位置发生了改变（例如，1 和 5）。
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 解释：请注意，nums 的值不一定唯一。
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        def maxHeapfy(nums: List[int], i, size):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                largest = i
                if left < size and nums[left] > nums[largest]:
                    largest = left
                if right < size and nums[right] > nums[largest]:
                    largest = right
                if largest == i:
                    break

                nums[largest], nums[i] = nums[i], nums[largest]
                i = largest

        for i in range(n//2 - 1, -1, -1):
            maxHeapfy(nums, i, n)

        for end in range(n - 1, -1, -1):
            nums[end], nums[0] = nums[0], nums[end]
            maxHeapfy(nums, 0, end)

        return nums

if __name__ == "__main__":
    s = Solution()
    tests = [
        [5,2,3,1],
        [5,1,1,2,0,0],
        [10,9,8,7,6,5,4,3,2,1],
        [],
        [1]
    ]

    for t in tests:
        print("输入:", t)
        print("输出:", s.sortArray(t[:]))  # 用切片避免原数组被改动
        print()
