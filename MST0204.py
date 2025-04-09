# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，
# 使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你不需要 保留 每个分区中各节点的初始相对位置

# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]

# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 你可以将链表拆分成两个子链表：
#
# 一个存储所有值小于 x 的节点，
#
# 一个存储所有值大于等于 x 的节点。
#
# 最后把这两个链表拼接起来即可。

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_small_head = ListNode(0)
        dummy_large_head = ListNode(0)

        small_head = dummy_small_head
        large_head = dummy_large_head

        current = head
        while current:
            if current.val < x:
                small_head.next = current
                small_head = small_head.next
            else:
                large_head.next = current
                large_head = large_head.next
            current = current.next

        small_head.next = dummy_large_head.next
        large_head.next = None

        return dummy_small_head.next

# 辅助函数：将列表转为链表
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 辅助函数：将链表转为列表，方便输出结果
def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == '__main__':
    # 测试用例
    sol = Solution()
    test1 = list_to_linkedlist([1, 4, 3, 2, 5, 2])
    res1 = sol.partition(test1, 3)
    print(linkedlist_to_list(res1))  # 可能输出: [1, 2, 2, 4, 3, 5]

    test2 = list_to_linkedlist([2, 1])
    res2 = sol.partition(test2, 2)
    print(linkedlist_to_list(res2))  # 可能输出: [1, 2]
