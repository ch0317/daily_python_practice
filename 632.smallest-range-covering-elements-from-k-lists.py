# 你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
#
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
#
#
#
# 示例 1：
#
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释：
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 示例 2：
#
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
#
#
# 提示：
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] 按非递减顺序排列


import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 示例测试
        k = len(nums)
        pq = []
        current_max = float('-inf')
        for i in range(k):
            heapq.heappush(pq, (nums[i][0],i,0))
            current_max = max(current_max, nums[i][0])

        best_range = [float('-inf'), float('inf')]

        while True:
            cur_min, list_idx, elem_idx = heapq.heappop(pq)
            if (current_max - cur_min < best_range[1] - best_range[0]) or (
                    current_max - cur_min == best_range[1] - best_range[0] and cur_min < best_range[0]
            ):
                best_range = [cur_min, current_max]
            if elem_idx + 1 == len(nums[list_idx]):
                break
            next_elem = nums[list_idx][elem_idx + 1]
            heapq.heappush(pq, (next_elem, list_idx, elem_idx + 1))
            current_max = max(current_max, next_elem)

        return best_range


if __name__ == '__main__':
    # 示例测试
    s = Solution()

    nums1 = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(s.smallestRange(nums1))  # 预期输出 [20,24]

    nums2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(s.smallestRange(nums2))  # 预期输出 [1,1]

    nums3 = [[1], [2], [3]]
    print(s.smallestRange(nums3))  # 预期输出 [1,3]

