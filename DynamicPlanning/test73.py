"""
@Author : SakuraFox
@Time: 2024-09-02 20:49
@File : test73.py
@Description : 343. 整数拆分(思路代码抄)
1.意义:i-数字,dp[i]-最大乘积
2.dp[i]=ma(dp[i],max(j*(i-j),j*dp[i-j])),dp[i-j]:前几次的拆分
3.dp[2]=1, dp[0]和dp[1]无意义,所以i从3开始遍历
4.数字从小到大
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(i // 2 + 1):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
