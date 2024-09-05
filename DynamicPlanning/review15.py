"""
@Author : SakuraFox
@Time: 2024-09-05 20:47
@File : review15.py
@Description : 62.不同路径、63. 不同路径 II、343. 整数拆分-复习-1

62.不同路径考虑遍历时从1开始，而不是0
63. 不同路径卡在初始化赋值重点为障碍的情况
343. 整数拆分卡在j*(i-j)为数字一个一个切割,dp[i-j]*j不太理解

"""
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for x in range(m):
            dp[x][0] = 1
        for y in range(n):
            dp[0][y] = 1
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        print(dp[m - 1][n - 1])
        return dp[m - 1][n - 1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), dp[i - j] * j)
            print(dp[i])
        return dp[n]
