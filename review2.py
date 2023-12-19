# 707.设计链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        temp = self.dummy_head.next
        for i in range(index):
            temp = temp.next
        return temp.val

    def addAtTail(self, val: int) -> None:
        temp = self.dummy_head
        for i in range(self.size):
            temp = temp.next
        temp.next = ListNode(val=val, next=None)
        self.size += 1
        return temp

    def addAtHead(self, val: int) -> None:
        self.dummy_head = ListNode(val=val, next=self.dummy_head)
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
        if self.size<0 or index > self.size:
            return
        dumpy = ListNode(next=self.dummy_head)
        for i in range(index):
            dumpy = dumpy.next
        dumpy.next = dumpy.next.next
        self.size -= 1

mylink = MyLinkedList()
mylink.addAtTail(6)
mylink.addAtTail(5)
mylink.addAtTail(4)
mylink.addAtTail(8)
for i in range(mylink.size):
    print(mylink.get(i))
print('-------------------------')
mylink.deleteAtIndex(3)
for i in range(mylink.size):
    print(mylink.get(i))

