# 给定一个链表，删除链表的倒数第n
# 个结点，并且返回链表的头结点。
from MST0204 import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        dummy = ListNode(0)
        dummy.next = head

        for _ in range(n):
            fast = fast.next

        pre = dummy
        while fast:
            fast = fast.next
            pre = slow
            slow = slow.next

        pre.next = slow.next

        return dummy.next

# 辅助函数：构造链表
def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 辅助函数：链表转数组
def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 测试样例
if __name__ == '__main__':
    head = build_list([1, 2, 3, 4, 5])
    n = 2
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    print("结果链表:", list_to_array(new_head))  # 期望输出: [1, 2, 3, 5]