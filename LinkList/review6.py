"""
@Author : SakuraFox
@Time: 2024-06-07 8:53
@File : review6.py
@Description : 203. 移除链表元素(思路基本正确,但代码照着敲了一遍)
注意:
1.添加头节点
2.遍历时从头节点的下一个节点开始
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(next=head)
        cur = root
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return root.next
