"""
@Author : SakuraFox
@Time: 2024-08-22 20:41
@File : test70.py
@Description : 746. 使用最小花费爬楼梯（抄）
思路:
1.意义:爬i阶最少花费dp[i]体力
2.公式:dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
3.初始化:根据题意得
4.从前往后

"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        print(dp)
        return dp[len(dp) - 1]
