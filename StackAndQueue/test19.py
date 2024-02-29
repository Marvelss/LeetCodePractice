# 225. 用队列实现栈
from collections import deque


class MyStack:

    def __init__(self):
        self.queen_in = deque()
        self.queen_out = deque()

    def push(self, x: int) -> None:
        self.queen_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return 0
        for i in range(len(self.queen_in) - 1):
            self.queen_out.append(self.queen_in.popleft())
        self.queen_in, self.queen_out = self.queen_out, self.queen_in
        return self.queen_out.popleft()

    # 和pop类似,只不过将元素弹出后放回
    def top(self) -> int:
        if self.empty():
            return 0
        for i in range(len(self.queen_in) - 1):
            self.queen_out.append(self.queen_in.popleft())
        self.queen_in, self.queen_out = self.queen_out, self.queen_in
        temp = self.queen_out.popleft()
        self.queen_in.append(temp)
        return temp

    def empty(self) -> bool:
        return len(self.queen_in) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
