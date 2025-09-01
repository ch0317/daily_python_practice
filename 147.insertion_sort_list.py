# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
#
# 插入排序 算法的步骤:
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。
#
# 对链表进行插入排序。
from MST0204 import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        lastSorted = head
        cur = head.next

        while cur:
            if cur.val >= lastSorted.val:
                lastSorted = lastSorted.next
            else:
                pre = dummy
                while pre.next and pre.next.val <= cur.val:
                    pre = pre.next
                lastSorted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = lastSorted.next

        return dummy.next

# 辅助函数：构造链表
def build_linked_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# 辅助函数：打印链表
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(" -> ".join(map(str, vals)))


# ========== 测试代码 ==========
if __name__ == "__main__":
    s = Solution()

    # 测试1：普通乱序
    head = build_linked_list([4, 2, 1, 3])
    print("原链表:")
    print_linked_list(head)
    sorted_head = s.insertionSortList(head)
    print("排序后:")
    print_linked_list(sorted_head)
    print()

    # 测试2：已经有序
    head = build_linked_list([1, 2, 3, 4])
    print("原链表:")
    print_linked_list(head)
    sorted_head = s.insertionSortList(head)
    print("排序后:")
    print_linked_list(sorted_head)
    print()

    # 测试3：逆序
    head = build_linked_list([5, 4, 3, 2, 1])
    print("原链表:")
    print_linked_list(head)
    sorted_head = s.insertionSortList(head)
    print("排序后:")
    print_linked_list(sorted_head)
    print()

    # 测试4：含有重复元素
    head = build_linked_list([3, 3, 1, 2, 2])
    print("原链表:")
    print_linked_list(head)
    sorted_head = s.insertionSortList(head)
    print("排序后:")
    print_linked_list(sorted_head)