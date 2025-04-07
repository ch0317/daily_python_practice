# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# 构建链表的辅助函数
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 打印链表的辅助函数
def print_linked_list(head: Optional[ListNode]) -> None:
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# 测试
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = build_linked_list(values)
    print("原链表：")
    print_linked_list(head)

    solution = Solution()
    reversed_head = solution.reverseList(head)
    print("反转后链表：")
    print_linked_list(reversed_head)