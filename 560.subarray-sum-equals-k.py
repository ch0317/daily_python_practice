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
#
#
# 提示：
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_count = defaultdict(int)
        pre_sum = 0
        pre_count[0] = 1

        for num in nums:
            pre_sum += num
            if(pre_sum - k in pre_count):
                count += pre_count[pre_sum - k]
            pre_count[pre_sum] += 1
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