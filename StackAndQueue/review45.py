"""
@Author : SakuraFox
@Time: 2024-12-06 9:05
@File : review45.py
@Description : 239. 滑动窗口最大值（思路抄，代码半自己写）
思路：
1.使用队列
2.保持队列内元素单调递减（若入队元素比对内元素大，去除对内小元素再入队）
3.根据上述思路自定义入队、出队方法
注意：
que.pop(nums[i - k])  # 移除窗口外的元素（卡点）
"""
from collections import deque


class MyQueue:  # 单调队列（从大到小)
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        # 保持队列只含相对较大的元素在顶端
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        que = MyQueue()
        result = []
        # 先放入栈
        while i < k:
            que.push(nums[i])
            i += 1
        result.append(que.front())
        while i < len(nums):
            que.pop(nums[i - k])  # 移除窗口外的元素（卡点）
            que.push(nums[i])
            result.append(que.front())
            i += 1
        return result
