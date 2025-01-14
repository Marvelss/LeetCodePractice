"""
@Author : SakuraFox
@Time: 2025-01-14 18:56
@File : review73.py
@Description : 746. 使用最小花费爬楼梯（未想出递归公式）


1.i:台阶；dp[i]:爬上第i个台阶最小费用
2.dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
3.dp[0] = 0;dp[1]=0
4.正序
5.举例
"""
from typing import List

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        dp[0] =0
        dp[1] = 0
        for i in range(2,len(dp)):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        print(dp)
        return dp[len(dp)-1]
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[len(cost) - 1]
