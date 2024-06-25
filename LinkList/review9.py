"""
@Author : SakuraFox
@Time: 2024-06-25 21:28
@File : review9.py
@Description : 24. 两两交换链表中的节点（抄，晕头转向！）
思路：
1.4个为一循环（包括虚拟头节点）
2.步骤一:头->头.next.next
3.步骤二:头.next.next->头.next
4.步骤三:头.（直接看网址清楚）

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # h 1 2 3 4
        virtual_head = ListNode(next=head)
        cur = virtual_head
        while cur.next and cur.next.next:
            temp = cur.next  # 1
            temp1 = cur.next.next.next  # 3
            cur.next = cur.next.next  # h 1 2
            cur.next.next = temp1.next  # h 1 2 4
            temp.next = temp1  # h 1 3 2 4
            cur = cur.next.next
        return virtual_head.next
