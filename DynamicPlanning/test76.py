"""
@Author : SakuraFox
@Time: 2024-09-25 21:43
@File : test76.py
@Description : 416. 分割等和子集(抄)
理解dp[j] == j 转为0-1背包问题的关键
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        count = 0
        for n in nums:
            count += n
        if count % 2 == 1:
            return False
        target = count // 2
        dp = [False] * (target + 1)
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return True if dp[target] == target else False
