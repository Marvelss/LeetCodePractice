"""
@Author : SakuraFox
@Time: 2024-12-01 19:21
@File : review41.py
@Description : 225. 用队列实现栈-R1（POP思路抄）
思路：2个队列实现栈，in队列代表用于输入输出，out队列代表临时存储
1.push:in队列输入
2.pop:弹出in里除第一个弹入的所有元素至out，in和out队列转换
3.top:弹出顶部元素并放回
4.判断代表输入输出的in队列内容是否为空

"""
# 225. 用队列实现栈
from collections import deque


class MyStack:

    def __init__(self):
        self.queen_in = deque()
        self.queen_out = deque()

    def push(self, x: int) -> None:
        self.queen_in.append(x)

    def pop(self) -> int:
        if not len(self.queen_in):
            return 0
        for _ in range(len(self.queen_in) - 1):
            self.queen_out.append(self.queen_in.popleft())
        self.queen_in, self.queen_out = self.queen_out, self.queen_in
        return self.queen_out.popleft()
        # 和pop类似,只不过将元素不弹出


def top(self) -> int:
    result = self.pop()
    self.queen_in.append(result)
    return result


def empty(self) -> bool:
    return len(self.queen_in) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
