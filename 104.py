# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        depth = 0

        while q:
            level_size = len(q)
            for _ in range(level_size):
                front = q.popleft()
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
            depth += 1

        return depth



def build_tree():
    # 构造如下二叉树：
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

if __name__ == "__main__":
# 测试递归方法
    root = build_tree()
    solution_recursive = SolutionIterative()
    print("递归法最大深度:", solution_recursive.maxDepth(root))  # 输出: 3

    # 测试迭代方法
    solution_iterative = SolutionIterative()
    print("迭代法最大深度:", solution_iterative.maxDepth(root))  # 输出: 3