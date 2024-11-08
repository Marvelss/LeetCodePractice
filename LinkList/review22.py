"""
@Author : SakuraFox
@Time: 2024-11-08 8:57
@File : review22.py
@Description : 707. 设计链表-R2(细节上很多点需要注意)
注意：
1.考虑index边界值: index < 0 or index>self.size
2.在各分方法具体代码中标识
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
        # cur = self.dummy_head
        # dummy_head是虚拟头节点，且注意index指向的元素，同时考察for循环的range(index)不循环到
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        # self.dummy_head.next = ListNode(val=val, next=self.dummy_head)
        # 同样注意指向
        self.dummy_head.next = ListNode(val=val, next=self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curHead = self.dummy_head
        for _ in range(self.size):
            curHead = curHead.next
        curHead.next = ListNode(val=val, next=None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        cur.next = ListNode(val=val, next=cur.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size or index < 0:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        # 判断节点是否为空
        if cur.next is not None:
            cur.next = cur.next.next
            self.size -= 1
