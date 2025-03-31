# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2

# 你可以使用 前缀和 + 哈希表 来优化求解子数组和为 k 的个数问题，使时间复杂度达到 O(n)。
#
# 关键思想：
# 维护一个 prefix_sum 变量，表示数组的前缀和。
#
# 用哈希表 prefix_count 记录 某个前缀和出现的次数，用于快速查找满足 prefix_sum - k 的前缀出现的次数。
#
# 每遍历一个元素时，检查 prefix_sum - k 是否在 prefix_count 中，若存在则累加其出现次数。

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_count = defaultdict(int)
        prefix_sum = 0
        prefix_count[0] = 1

        for num in nums:
            prefix_sum += num

            if(prefix_sum - k in prefix_count):
                count += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1

        return count


if __name__ == "__main__":
    solution = Solution()

    # 测试用例 1
    nums = [1, 1, 1]
    k = 2
    assert solution.subarraySum(nums, k) == 2
    print("Test case 1 passed!")

    # 测试用例 2
    nums = [1, 2, 3]
    k = 3
    assert solution.subarraySum(nums, k) == 2
    print("Test case 2 passed!")

    # 测试用例 3: 只有一个元素
    nums = [1]
    k = 1
    assert solution.subarraySum(nums, k) == 1
    print("Test case 3 passed!")

    # 测试用例 4: 负数情况
    nums = [-1, -1, 1]
    k = 0
    assert solution.subarraySum(nums, k) == 1
    print("Test case 4 passed!")
