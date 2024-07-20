"""
@Author : SakuraFox
@Time: 2024-07-20 20:33
@File : test58.py
@Description : 55. 跳跃游戏
思路:每次跳的范围大于数组长度
小技巧:从正向考虑若范围大于长度,则T，否则F；每次更新覆盖范围
"""
from typing import List


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


Solution().canJump([3, 0, 0, 0])
