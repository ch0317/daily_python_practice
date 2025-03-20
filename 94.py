# 给定一个二叉树的根节点
# root ，返回
# 它的
# 中序
# 遍历 。
#
#
# 示例
# 1：
#
# 输入：root = [1, null, 2, 3]
# 输出：[1, 3, 2]
# 示例
# 2：
#
# 输入：root = []
# 输出：[]
# 示例
# 3：
#
# 输入：root = [1]
# 输出：[1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现中序遍历
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, result):
            if not root:
                return
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        result = []
        inorder(root, result)
        return result

    # 迭代实现中序遍历
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [],[]
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            print(result)
            current = current.right

        return result


# 辅助函数：构建二叉树（示例 [1, null, 2, 3]）
def buildTree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    children = nodes[::-1]
    root = children.pop()

    for node in nodes:
        if node:
            if children: node.left = children.pop()
            if children: node.right = children.pop()

    return root


# 测试代码
if __name__ == "__main__":
    # 测试用例1: [1, None, 2, 3]
    root1 = buildTree([1, None, 2, 3])
    solution = Solution()
    #print("递归中序遍历:", solution.inorderTraversalRecursive(root1))
    print("迭代中序遍历:", solution.inorderTraversalIterative(root1))

    # 测试用例2: []
    root2 = buildTree([])
    #print("递归中序遍历:", solution.inorderTraversalRecursive(root2))
    print("迭代中序遍历:", solution.inorderTraversalIterative(root2))

    # 测试用例3: [1]
    root3 = buildTree([1])
    #print("递归中序遍历:", solution.inorderTraversalRecursive(root3))
    print("迭代中序遍历:", solution.inorderTraversalIterative(root3))
