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
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
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
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# 创建一个链表
linked_list = MyLinkedList()

# 添加节点到链表头部
linked_list.addAtHead(1)
linked_list.addAtHead(2)
linked_list.addAtHead(3)
# 链表应该是 3 -> 2 -> 1
print('---------------添加节点到链表头部---------------')
for i in range(linked_list.size):
    print(linked_list.get(i))

# 添加节点到链表尾部
linked_list.addAtTail(4)
linked_list.addAtTail(5)
# 链表应该是 3 -> 2 -> 1 -> 4 -> 5
print('---------------添加节点到链表尾部---------------')
for i in range(linked_list.size):
    print(linked_list.get(i))
# 在指定位置添加节点
linked_list.addAtIndex(2, 6)
# 链表应该是 3 -> 2 -> 6 -> 1 -> 4 -> 5
print('---------------在指定位置添加节点---------------')
for i in range(linked_list.size):
    print(linked_list.get(i))
# 删除指定位置的节点
linked_list.deleteAtIndex(1)
# 链表应该是 3 -> 6 -> 1 -> 4 -> 5

print('---------------删除指定位置的节点---------------')
for i in range(linked_list.size):
    print(linked_list.get(i))
