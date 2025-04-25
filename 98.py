# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], max:float, min:float) -> bool:
            if not node:
                return True
            if node.val <= min:
                return False
            if node.val >= max:
                return False

            return helper(node.left, node.val, min) and helper(node.right, max, node.val)
        return helper(root, float('inf'), float('-inf'))


def test_isValidBST():
    sol = Solution()

    # 用例 1：空树，合法
    assert sol.isValidBST(None) == True

    # 用例 2：合法 BST
    #       2
    #      / \
    #     1   3
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert sol.isValidBST(root) == True

    # 用例 3：非法 BST
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert sol.isValidBST(root) == False

    # 用例 4：只有一个节点
    root = TreeNode(1)
    assert sol.isValidBST(root) == True

    # 用例 5：非法 BST，右子节点小于根节点
    #       10
    #         \
    #         5
    root = TreeNode(10, None, TreeNode(5))
    assert sol.isValidBST(root) == False

    print("所有测试用例通过！")

if __name__ == '__main__':
    test_isValidBST()