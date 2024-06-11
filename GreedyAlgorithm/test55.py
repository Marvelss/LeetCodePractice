"""
@Author : SakuraFox
@Time: 2024-06-11 21:43
@File : test55.py
@Description : 376. 摆动序列(抄)
1.总体思路
局部最优(前后峰值一大一小<0)------>全部最优(最长子序列的长度)
2.边界情况
2.1单调平坡
2.2上下平坡
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curDiff = 0
        preDiff = 0
        result = 1
        for i in range(len(nums) - 1):
            # 后值减前值
            curDiff = nums[i + 1] - nums[i]
            if (curDiff < 0 and preDiff >= 0) or (curDiff > 0 and preDiff <= 0):
                result += 1
                preDiff = curDiff
        return result
