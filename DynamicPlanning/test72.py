"""
@Author : SakuraFox
@Time: 2024-08-27 18:28
@File : test72.py
@Description : 63. 不同路径 II(代码思路抄)
思路
1.m,n:行,列   dp[m][n]:共有路径数量
2.dp[m][n] = dp[m-1][n]+ dp[m][n-1]
3.遇obstacleGrid[m - 1][n - 1] == 1或[0][0]==1:返回 0
重点:
1.首先行,列遍历:obstacleGrid[i][0] == 1|obstacleGrid[0][j],
遇障碍物时dp[i][0] = 0
2.然后与无障碍物时正常公式,if obstacleGrid[i][j] == 1:时跳过

"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
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
