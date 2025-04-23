# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。
# （即逐层地，从左到右访问所有节点）。
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]

# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = [[root.val]]
        queue = deque([root])

        while queue:
            q_size = len(queue)
            res = []
            for _ in range(q_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    res.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    res.append(node.right.val)
            if res:
                results.append(res)

        return results



# 辅助函数：将列表构建为二叉树
def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


# 测试用例
test_cases = [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ([1], [[1]]),
    ([], []),
]

if __name__ == '__main__':
    solution = Solution()
    for i, (input_list, expected_output) in enumerate(test_cases):
        tree = build_tree_from_list(input_list)
        output = solution.levelOrder(tree)
        print(f"Test Case {i + 1}: {'Pass' if output == expected_output else 'Fail'}")
        print(f"Expected: {expected_output}, Got: {output}\n")

