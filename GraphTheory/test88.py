"""
@Author : SakuraFox
@Time: 2024-10-28 13:23
@File : test88.py
@Description : 695. 岛屿的最大面积

在200. 岛屿数量的基础上，计算最大值
dfs判断是否为岛屿的相反情况

"""


class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(self, gridT, visitedT, x, y):
        m, n = len(gridT), len(gridT[0])
        count = 1
        visitedT[x][y] = True

        for o, p in self.dirs:
            nextX, nextY = x + o, y + p

            if 0 <= nextX < m and 0 <= nextY < n and not visitedT[nextX][nextY] and gridT[nextX][nextY] == 1:
                visitedT[nextX][nextY] = True
                count += self.dfs(gridT, visitedT, nextX, nextY)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    countT = self.dfs(grid, visited, i, j)
                    result = max(result, countT)
        return result
