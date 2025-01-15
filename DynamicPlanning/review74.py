"""
@Author : SakuraFox
@Time: 2025-01-15 16:36
@File : review74.py
@Description : 62.不同路径-R1

思路：
1.m:行；n:列；dp[m][n]:走到第m行第n列的路径数量
2.dp[m][n] = dp[m-1][n]+dp[m][n-1]
3.dp[0][n] = 1;dp[m][0]=1
4.正序
5.举例

注意点：
创建二维数组方式
① 原始版
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)
②列表推导式  dp = [[0]*n for _ in range(m)]

"""

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for x in range(m):
            dp[x][0]=1
        for y in range(n):
            dp[0][y]=1
        for x in range(1,m):
            for y in range(1,n):
                dp[x][y] = dp[x-1][y]+dp[x][y-1]
        print(dp[m-1][n-1])
        return dp[m-1][n-1]
       
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建二维数组
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)
        # 初始化
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                # print('-'*10)
                # print(f'{i}=={j}')
                # print(dp[i][j])
        return dp[m - 1][n - 1]
