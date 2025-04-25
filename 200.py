# 给你一个由
# '1'（陆地）和
# '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和 / 或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例
# 1：
#
# 输入：grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# 输出：1
# 示例
# 2：
#
# 输入：grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# 输出：3

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        def dfs(grid, i, j):
            col_num = len(grid[0])
            row_num = len(grid)
            if i < 0 or i >= row_num or j < 0 or j >= col_num:
                return 0
            if grid[i][j] == '1':
                grid[i][j] = 'x'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
                return 1
            else:
                return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num += dfs(grid, i, j)

        return num

def test_numIslands():
    sol = Solution()

    # 示例用例 1：只有一个岛
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert sol.numIslands([row[:] for row in grid1]) == 1  # 使用 row[:] 避免原数组被修改

    # 示例用例 2：三个岛
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert sol.numIslands([row[:] for row in grid2]) == 3

    # 边界测试：空网格
    grid3 = []
    assert sol.numIslands(grid3) == 0

    # 边界测试：全是水
    grid4 = [
        ["0", "0"],
        ["0", "0"]
    ]
    assert sol.numIslands(grid4) == 0

    # 边界测试：全是陆地
    grid5 = [
        ["1", "1"],
        ["1", "1"]
    ]
    assert sol.numIslands([row[:] for row in grid5]) == 1

    print("所有测试用例通过！")

if __name__ == '__main__':
    test_numIslands()
