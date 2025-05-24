# 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
# 示例 2:
#
# 输入: head = []
# 输出: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional,List
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMiddle(start: Optional[ListNode]):
            prev = None
            fast = slow = start
            while fast and fast.next:
                prev = slow
                fast = fast.next.next
                slow = slow.next
            # important
            if prev:
                prev.next = None

            return slow

        if head is None:
            return None

        mid = findMiddle(head)
        root = TreeNode(mid.val)

        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

# 测试辅助函数
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def tree_to_list_preorder(root: Optional[TreeNode]) -> List[Optional[int]]:
    result = []
    def preorder(node):
        if not node:
            result.append(None)
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    # 去掉末尾多余的 None（为了比较）
    while result and result[-1] is None:
        result.pop()
    return result

# 测试用例
def test():
    s = Solution()

    head1 = list_to_linkedlist([-10, -3, 0, 5, 9])
    tree1 = s.sortedListToBST(head1)
    print("Test 1:", tree_to_list_preorder(tree1))

    head2 = list_to_linkedlist([])
    tree2 = s.sortedListToBST(head2)
    print("Test 2:", tree_to_list_preorder(tree2))

    head3 = list_to_linkedlist([1])
    tree3 = s.sortedListToBST(head3)
    print("Test 3:", tree_to_list_preorder(tree3))

if __name__ == '__main__':
    test()