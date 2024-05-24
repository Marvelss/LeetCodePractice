"""
@Author : SakuraFox
@Time: 2024-05-24 19:49
@File : review2.py
@Description : 27. 移除元素-复习-1
技巧：双指针
快指针自转,慢指针根据快指针的值动
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
