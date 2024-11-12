"""
@Author : SakuraFox
@Time: 2024-11-12 14:16
@File : review25.py
@Description : 19. 删除链表的倒数第 N 个结点-R2(思路抄，按照思路代码自写)
思路：双指针-提前让fast先走n步
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = ListNode(next=head)
        fast = cur
        slow = cur
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 替换
        slow.next= slow.next.next
        return cur.next