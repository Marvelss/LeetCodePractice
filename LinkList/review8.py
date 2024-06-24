"""
@Author : SakuraFox
@Time: 2024-06-24 21:39
@File : review8.py
@Description : 206. 反转链表
注意:
1.思想与数组两元素交换位置类似
2.注意每个要素代表内容
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return cur
