# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
# 同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
# 提示：
#
# 树中节点数目范围是 [1, 3 * 104]
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    maxPath = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))

            maxVal = max(left, right)
            self.maxPath = max(self.maxPath, root.val + left + right)

            return root.val + maxVal
        dfs(root)

        return self.maxPath

# 辅助函数：构建二叉树
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == '__main__':
    # 测试示例
    root1 = build_tree([1,2,3])
    root2 = build_tree([-10,9,20,None,None,15,7])
    root3 = build_tree([-3])

    sol = Solution()
    print(sol.maxPathSum(root1))  # 输出：6
    sol = Solution()
    print(sol.maxPathSum(root2))  # 输出：42
    sol = Solution()
    print(sol.maxPathSum(root3))  # 输出：-3