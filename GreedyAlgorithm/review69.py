"""
@Author : SakuraFox
@Time: 2025-01-10 10:25
@File : review69.py
@Description : 55. 跳跃游戏-R1(思路对，但代码没写出来)

思路：
局部最优：每次取最大跳跃步数（取最大覆盖范围）
全局最优：整体最大覆盖范围

关键点（代码未写出原因）：while i <= cover:(终止条件为cover)
cover每走一步都在判断，若大于数组长度，则可行；若结束循环则说明中途漏油了，到达不到终点
"""
from typing import List

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= step:
                step = max(i + nums[i], step)
                if step >= len(nums) - 1:
                    return True
        return False

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False
