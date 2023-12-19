# 链表相交
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_len, b_len = 0, 0
        tempA = headA
        tempB = headB
        while tempA:
            tempA = tempA.next
            a_len += 1
        while tempB:
            tempB = tempB.next
            b_len += 1
        curA, curB = headA, headB
        if a_len > b_len:
            curA, curB = curB, curA
            a_len, b_len = b_len, a_len
        for _ in range(b_len - a_len):
            curB = curB.next
        while curA:
            if curB == curA:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
