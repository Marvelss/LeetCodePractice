"""
@Author : SakuraFox
@Time: 2025-01-15 16:57
@File : review75.py
@Description : 63. 不同路径 II(很棒独立调试后写完)-R1

思路：与62. 不同路径一致，不同点在下方注意点
1.m:行；n:列；dp[m][n]:走到第m行第n列的路径数量
2.dp[m][n] = dp[m-1][n]+dp[m][n-1]
3.dp[0][n] = 1;dp[m][0]=1
4.正序
5.举例

注意点：
1.初始化时，若obstacleGrid[i][j]==1，则（**往后**）所有dp[i][j]都为0
2.动态规划计算dp[i][j]时，若obstacleGrid[i][j]==1，则跳过对应dp[i][j]的计算（因为赋值时默认为0，不影响后续值相加）

"""
from typing import List

"""
class Solution:
     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        # 二维数组创建
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        # 初始化
        # 行
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        # 列
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        print(dp)
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
