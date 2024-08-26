"""
@Author : SakuraFox
@Time: 2024-08-26 19:17
@File : test71.py
@Description : 62. 不同路径(抄)
思路
1.字母代表意义:i,j对应行,dp[i][j]不同路径总数
2.公式:dp[i][j]= dp[i-1][j]+dp[i][j-1]
3.初始化:dp[0][n]和dp[m][0]整一行/列输出都为1
4.走左边和下标方向=从左往右遍历(下标从小到大)

注意:
1.创建m×n维数组
for _ in range(m):
 dp.append([0] * n)
2.返回值的边界值dp[m-1][n-1]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
