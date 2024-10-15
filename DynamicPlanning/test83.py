"""
@Author : SakuraFox
@Time: 2024-10-15 20:08
@File : test83.py
@Description : 279.完全平方数
要点:
1.平方数:dp[j-i*i]
2.dp[j]完全平方数的最少数量:min(dp[j-i*i]+1,dp[j])
3.初始赋值无穷小,因为min
4.先遍历背包后物品:遍历物品时---->for j in range(1, int(i ** 0.5) + 1)
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if j * j <= i:
                    dp[i] = min(dp[i - j * j] + 1, dp[i])
        return dp[n]