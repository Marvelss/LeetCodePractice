"""
@Author : SakuraFox
@Time: 2024-11-08 13:29
@File : review23.py
@Description : 206. 反转链表-R2（逻辑还需盘一盘）
注意：Pre会随着循环变动,头节点
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tempNext = cur.next
            cur.next = pre
            pre = cur
            cur = tempNext
        return pre
