# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List,Optional
# Definition for singly-linked list.

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

# 辅助函数：将 Python 列表转换为链表
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 辅助函数：将链表转换为 Python 列表
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == '__main__':
    # 测试用例
    sol = Solution()

    # 示例 1
    l1 = list_to_linkedlist([1,2,4])
    l2 = list_to_linkedlist([1,3,4])
    merged = sol.mergeTwoLists(l1, l2)
    print(linkedlist_to_list(merged))  # 输出：[1,1,2,3,4,4]

    # 示例 2
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([])
    merged = sol.mergeTwoLists(l1, l2)
    print(linkedlist_to_list(merged))  # 输出：[]

    # 示例 3
    l1 = list_to_linkedlist([])
    l2 = list_to_linkedlist([0])
    merged = sol.mergeTwoLists(l1, l2)
    print(linkedlist_to_list(merged))  # 输出：[0]
