# 203.移除链表元素
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(6)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
head1.next.next.next.next.next.next = ListNode(6)

solution = Solution()
result4 = solution.removeElements(head1, 5)
while result4:
    print(result4.val)
    result4 = result4.next