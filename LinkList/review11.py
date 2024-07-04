"""
@Author : SakuraFox
@Time: 2024-07-04 19:21
@File : review11.py
@Description : 面试题 02.07. 链表相交
暴力方法对其链表
注意：curA == curB节点相对而不值相等
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        tempA, tempB = headA, headB
        while tempA:
            tempA = tempA.next
            lenA += 1
        while tempB:
            tempB = tempB.next
            lenB += 1

        curA = headA
        curB = headB
        if lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        else:
            for i in range(lenA - lenB):
                curA = curA.next

        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
