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
from heapq import merge
from typing import List

class Solution:

    def merge(self, nums: List[int], p:int, q: int, r: int):
        Len1 = q - p + 1
        Len2 = r - q

        left_part = nums[p:q +1]
        right_part = nums[q + 1: r + 1]

        l,r,k = 0,0,p

        while l<Len1 and r<Len2:
            if left_part[l] <= right_part[r]:
                nums[k] = left_part[l]
                l += 1
            else:
                nums[k] = right_part[r]
                r += 1
            k = k + 1

        while l<Len1:
            nums[k] = left_part[l]
            l += 1
            k += 1

        while r<Len2:
            nums[k] = right_part[r]
            r += 1
            k += 1


    def mergeSort(self, nums: List[int], l : int,  r : int) -> None:
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.merge(nums, l, m, r)


    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
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
