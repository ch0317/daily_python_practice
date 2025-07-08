# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
# 提示：
#
# 1 <= heights.length <=105
# 0 <= heights[i] <= 104


from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height*width)
            stack.append(i)

        return max_area

# ===================
# ✅ 测试示例
# ===================
if __name__ == "__main__":
    s = Solution()
    heights1 = [2, 1, 5, 6, 2, 3]
    print(s.largestRectangleArea(heights1))  # 输出: 10

    heights2 = [2, 4]
    print(s.largestRectangleArea(heights2))  # 输出: 4

    # 额外测试
    heights3 = [0, 1, 0, 1]
    print(s.largestRectangleArea(heights3))  # 输出: 1

    heights4 = [1, 1, 1, 1]
    print(s.largestRectangleArea(heights4))  # 输出: 4

    heights5 = [4, 2, 0, 3, 2, 5]
    print(s.largestRectangleArea(heights5))  # 输出: 6
