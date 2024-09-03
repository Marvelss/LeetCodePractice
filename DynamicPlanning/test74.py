"""
@Author : SakuraFox
@Time: 2024-09-03 21:57
@File : test74.py
@Description : 96. 不同的二叉搜索树(思路代码抄)
难!需要再次理解
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for j in range(i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
