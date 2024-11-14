"""
@Author : SakuraFox
@Time: 2024-11-14 14:27
@File : review27.py
@Description : 142. 环形链表 II-R1(抄)
思路：
1.判断有环
2.判断环入口
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 判断有环
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # 找到节点
            if slow == fast:
                # 判断环入口
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
