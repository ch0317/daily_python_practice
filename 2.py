# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 解决方案
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy_head = ListNode()
        current = Dummy_head
        carry = 0
        value = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = carry + val1 + val2
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next



        return Dummy_head.next


# 辅助函数：将列表转为链表
def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# 辅助函数：将链表转为列表
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# 测试用例
def test():
    s = Solution()

    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # 输出: [7, 0, 8]

    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # 输出: [0]

    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = s.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # 输出: [8,9,9,9,0,0,0,1]


# 运行测试
if __name__ == '__main__':
    test()

