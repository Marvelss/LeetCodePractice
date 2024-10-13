"""
@Author : SakuraFox
@Time: 2024-10-11 19:10
@File : test79.py
@Description : 474.一和零(抄,几乎不了解)
定义:i个0j个1的str的最大子集大小为dp[i][j]
公式:dp[i][j] = max(dp[i][j],dp[i-zeroNum][j-oneNum] + 1)
初始化:全为0
遍历顺序:从后往前
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        zeroNum, oneNum = 0, 0
        for num in strs:
            if num == '0':
                zeroNum += 1
            else:
                oneNum += 1
            for i in range(m, zeroNum-1, -1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)
        return dp[m][n]
