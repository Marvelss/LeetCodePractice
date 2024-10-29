"""
@Author : SakuraFox
@Time: 2024-10-29 18:06
@File : test89.py
@Description : 1020. 飞地的数量
思路：先将靠边的陆地变为海洋,剩下的则为飞地
"""
from typing import List


class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(self, gridT, visitedT, x, y):
        visitedT[x][y] = 1
        for dx, dy in self.dirs:
            nextX, nextY = x + dx, y + dy
            if nextX < 0 or nextY < 0 or nextX >= len(gridT) or nextY >= len(gridT[0]):
                continue
            if not visitedT[nextX][nextY] and gridT[nextX][nextY] == 1:
                self.dfs(gridT, visitedT, nextX, nextY)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        # 先遍历上下两边
        for i in range(m):
            if not visited[i][0] and grid[i][0] == 1:
                self.dfs(grid, visited, i, 0)
            if not visited[i][n-1] and grid[i][n-1] == 1:
                self.dfs(grid, visited, i, n-1)
        # 再标记左右两边
        for j in range(n):
            if not visited[0][j] and grid[0][j] == 1:
                self.dfs(grid, visited, 0, j)
            if not visited[m-1][j] and grid[m-1][j] == 1:
                self.dfs(grid, visited, m-1, j)
        result = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    result += 1
        return result

