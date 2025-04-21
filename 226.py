# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        return root

# 层序遍历输出二叉树结构
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去除末尾的 None
    while result and result[-1] is None:
        result.pop()
    return result

# 构建二叉树的辅助函数（从列表构建二叉树，按层序）
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    tree_vals = [4, 2, 7, 1, 3, 6, 9]
    root = build_tree(tree_vals)
    solution = Solution()
    inverted_root = solution.invertTree(root)
    print(level_order_traversal(inverted_root))  # 输出应为 [4, 7, 2, 9, 6, 3, 1]