"""
@Author : SakuraFox
@Time: 2024-11-06 20:08
@File : review21.py
@Description : 203. 移除链表元素(难以AC)
卡点：
1.如果等于删除节点，则cur.next = cur.next.next；否则cur=cur.next
cur.next = cur.next.next已经在动节点了
2.cur 和root虚拟节点，cur会变动，root不会
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        subHeader = ListNode(next=head)
        cur = subHeader
        while cur.next:
            if cur.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return cur.next
