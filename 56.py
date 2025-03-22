# 以数组
# intervals
# 表示若干个区间的集合，其中单个区间为
# intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回
# 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例
# 1：
#
# 输入：intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# 输出：[[1, 6], [8, 10], [15, 18]]
# 解释：区间[1, 3]
# 和[2, 6]
# 重叠, 将它们合并为[1, 6].
# 示例
# 2：
#
# 输入：intervals = [[1, 4], [4, 5]]
# 输出：[[1, 5]]
# 解释：区间[1, 4]
# 和[4, 5]
# 可被视为重叠区间。


from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 先排序，保证每次遍历时当前区间的起始点比上一个区间靠后或相连。
        # 如果当前区间与结果列表的最后一个区间有重叠（即
        # merged[-1][1] >= interval[0]），合并它们。
        # 如果没有重叠，直接加入结果列表。
        merged = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == "__main__":
    s = Solution()

    # 示例1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = s.merge(intervals1)
    print(f"输入：{intervals1}")
    print(f"输出：{result1}\n")

    # 示例2
    intervals2 = [[1, 4], [4, 5]]
    result2 = s.merge(intervals2)
    print(f"输入：{intervals2}")
    print(f"输出：{result2}\n")

    # 补充测试用例
    intervals3 = [[1, 4], [5, 6]]
    result3 = s.merge(intervals3)
    print(f"输入：{intervals3}")
    print(f"输出：{result3}\n")

    intervals4 = [[1, 4], [0, 4]]
    result4 = s.merge(intervals4)
    print(f"输入：{intervals4}")
    print(f"输出：{result4}\n")

    intervals5 = [[1, 4], [2, 3]]
    result5 = s.merge(intervals5)
    print(f"输入：{intervals5}")
    print(f"输出：{result5}\n")
