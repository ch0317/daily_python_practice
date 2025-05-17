# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Dummy_head = ListNode()
        Dummy_head.next = head
        fast = Dummy_head
        slow = Dummy_head
        for _ in range(n):
            fast = fast.next

        pre = slow
        while fast != None:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next

        return Dummy_head.next
