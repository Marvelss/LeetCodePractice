"""
@Author : SakuraFox
@Time: 2024-06-20 21:17
@File : review7.py
@Description : 707. 设计链表

注意:
①各项index和self.size的初始值判别
②get方法的边界值和从头节点的.next节点开始
if index < 0 or index >= self.size:
current = self.dummy_head.next
③注意self.size的变化
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        tail_node = self.dummy_head
        for i in range(self.size):
            tail_node = tail_node.next
        tail_node.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummy_head
        for i in range(index):
            current = current.next
        if current.next != None:
            current.next = current.next.next
            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
