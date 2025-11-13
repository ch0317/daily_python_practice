# 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 质数 组成，且其中所有整数互不相同。
#
# 对于每对满足 0 <= i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
#
# 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。
#
#
# 示例 1：
#
# 输入：arr = [1,2,3,5], k = 3
# 输出：[2,5]
# 解释：已构造好的分数,排序后如下所示:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3
# 很明显第三个最小的分数是 2/5
# 示例 2：
#
# 输入：arr = [1,7], k = 1
# 输出：[1,7]
#
#
# 提示：
#
# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 104
# arr[0] == 1
# arr[i] 是一个 质数 ，i > 0
# arr 中的所有数字 互不相同 ，且按 严格递增 排序
# 1 <= k <= arr.length * (arr.length - 1) / 2
# 思路：
#
# 所有分数 arr[i]/arr[j]（i<j）其实都可以看作二维矩阵的一部分：
#
# 行是分子（i）
#
# 列是分母（j）
#
# 每行都是递增的（因为分母越大，分数越小）
#
# 使用最小堆来合并 k 个最小分数：
#
# 初始时，把所有 i = 0（分子为 arr[0]）对应的分数 arr[0]/arr[j] 放入堆。
#
# 每次弹出最小的分数 (i, j)，如果 i+1 < j，则把 (i+1, j) 入堆。
#
# 重复 k-1 次，最后堆顶就是第 k 个分数。
import heapq
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []
        n = len(arr)
        for j in range(1, n):
            heapq.heappush(pq, (arr[0] / arr[j], 0, j))

        for _ in range(k - 1):
            f, i, j = heapq.heappop(pq)
            if i + 1 < j:
                heapq.heappush(pq, (arr[i + 1] / arr[j], i + 1, j))

        _,i,j = heapq.heappop(pq)
        return [arr[i], arr[j]]

if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallestPrimeFraction([1, 2, 3, 5], 3))  # [2, 5]
    print(s.kthSmallestPrimeFraction([1, 7], 1))        # [1, 7]
    print(s.kthSmallestPrimeFraction([1, 2, 3, 5, 7, 11], 7))