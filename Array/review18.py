"""
@Author : SakuraFox
@Time: 2024-11-04 19:13
@File : review18.py
@Description : 27. 移除元素-R2
重点：快指针-遍历元素，慢指针-存放目标输出元素
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowIndex, fastIndex = 0, 0
        while fastIndex < len(nums):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
            fastIndex += 1
        return slowIndex
