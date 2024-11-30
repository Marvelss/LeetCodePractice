"""
@Author : SakuraFox
@Time: 2024-11-30 20:41
@File : review40.py
@Description : 232. 用栈实现队列-R1
思路：
1.push:放入stack_in
2.pop:若stack_out有值，则先pop，否则将stack_in元素一如stack_out并返回
3.peek:利用pop弹出元素，并放回
4.empty:判断两个队列是否为空
"""


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        result = self.pop()
        self.stack_out.append(result)
        return result

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
