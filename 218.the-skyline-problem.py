# 城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。
#
# 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：
#
# lefti 是第 i 座建筑物左边缘的 x 坐标。
# righti 是第 i 座建筑物右边缘的 x 坐标。
# heighti 是第 i 座建筑物的高度。
# 你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。
#
# 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
# 关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。
# 此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#
# 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
# 三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

# 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# 解释：
# 图 A 显示输入的所有建筑物的位置和高度，
# 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
# 示例 2：
#
# 输入：buildings = [[0,2,3],[2,5,3]]
# 输出：[[0,3],[5,0]]

from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, h in buildings:
            events.append([left, -h])
            events.append([right,h])

        events.sort(key=lambda x: (x[0], x[1]))

        heap = [0]
        active_height = {0: 1}
        pre_max = 0
        max_height = 0
        result = []

        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
                active_height[-h] = active_height.get(-h, 0) + 1
            else:
                active_height[h] -= 1

            while heap and active_height.get(-heap[0], 0) == 0:
                heapq.heappop(heap)

            max_height = -heap[0]

            if max_height != pre_max:
                pre_max = max_height
                result.append([x,max_height])

        return result

if __name__ == "__main__":
    sol = Solution()

    # 示例 1
    buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print("输入:", buildings1)
    print("输出:", sol.getSkyline(buildings1))
    # 期望输出: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

    # 示例 2
    buildings2 = [[0,2,3],[2,5,3]]
    print("输入:", buildings2)
    print("输出:", sol.getSkyline(buildings2))
    # 期望输出: [[0,3],[5,0]]

    # 示例 3（只有一栋楼）
    buildings3 = [[1,5,4]]
    print("输入:", buildings3)
    print("输出:", sol.getSkyline(buildings3))
    # 期望输出: [[1,4],[5,0]]

    # 示例 4（重叠建筑）
    buildings4 = [[1,10,3],[2,9,8],[3,8,6]]
    print("输入:", buildings4)
    print("输出:", sol.getSkyline(buildings4))
    # 期望输出: [[1,3],[2,8],[9,3],[10,0]]