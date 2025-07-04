# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 示例 2：
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
#
# 输入：nums = [1,0,1,2]
# 输出：3
#
#
# 提示：
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# 📌 核心思路：
# 用 哈希集合（set） 来快速判断某个数是否存在。
#
# 只在某个数是序列起点（即 num - 1 不在集合里）的时候开始向右扩展。
#
# 这样，每个数最多只被访问一次，时间复杂度是 O(n)。

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                result = max(current_length, result)

        return result



if __name__ == "__main__":
    s = Solution()
    # 示例 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(nums1))  # 输出 4

    # 示例 2
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    print(s.longestConsecutive(nums2))  # 输出 9

    # 示例 3
    nums3 = [1,0,1,2]
    print(s.longestConsecutive(nums3))  # 输出 3

    # 边界情况：空数组
    nums4 = []
    print(s.longestConsecutive(nums4))  # 输出 0

    # 边界情况：只有一个数
    nums5 = [10]
    print(s.longestConsecutive(nums5))  # 输出 1

    # 重复元素情况
    nums6 = [1,2,0,1]
    print(s.longestConsecutive(nums6))  # 输出 3
