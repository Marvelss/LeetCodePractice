from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextN=None):
        self.val = val
        self.nextN = nextN


class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp_head = ListNode(nextN=head)

        current = temp_head
        while current.nextN:
            if current.nextN.val == val:
                current.nextN = current.nextN.nextN
            else:
                current = current.nextN
        return temp_head.nextN

# 创建链表
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(6)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

head.nextN = node1
node1.nextN = node2
node2.nextN = node3
node3.nextN = node4
node4.nextN = node5
node5.nextN = node6
# 要删除的值
val = 6
new_head = Solution.removeElements(head, val)
current = new_head
while current:
    print(current.val)
    current = current.nextN
