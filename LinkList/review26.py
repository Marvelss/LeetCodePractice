"""
@Author : SakuraFox
@Time: 2024-11-13 15:39
@File : review26.py
@Description : 面试题 02.07. 链表相交-R2
注意：不考虑两链表相交后存在不相交的节点
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        indexA, indexB = 0, 0
        # 计算长度
        while curA:
            indexA += 1
            curA = curA.next
        while curB:
            indexB += 1
            curB = curB.next
        # 齐平
        if indexA > indexB:
            for _ in range(indexA - indexB):
                headA = headA.next
        else:
            for _ in range(indexB - indexA):
                headB = headB.next
        # 计算相同点
        while headB:
            if headA == headB:
                return headA
            else:
                headB = headB.next
                headA = headA.next
