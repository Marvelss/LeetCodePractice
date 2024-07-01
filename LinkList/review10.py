"""
@Author : SakuraFox
@Time: 2024-07-01 22:01
@File : review10.py
@Description : 19. 删除链表的倒数第 N 个结点(思路抄)
技巧:
1.双指针
注意:
1.虚拟节点
2.fast走n+1步
3.慢指针按照常规节点删除思路操作
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        vHead = ListNode(next=head)
        slow = vHead
        fast = vHead
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return vHead.next
