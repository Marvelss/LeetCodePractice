"""
@Author : SakuraFox
@Time: 2024-11-11 19:25
@File : review24.py
@Description : 24. 两两交换链表中的节点-R2
思路:在206. 反转链表上3各元素转换
小技巧：
1.引入dummyHead（该元素不动）
2.根据预期目标元素，一步一步调换dummyHead指针（关键考虑每个节点下一步指向谁）
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        cur = dummyHead
        while cur.next and cur.next.next:
            curIndex = cur.next.next.next
            n1 = cur.next
            cur.next = cur.next.next
            cur.next.next = n1
            n1.next = curIndex

            cur = cur.next.next
        return dummyHead.next
