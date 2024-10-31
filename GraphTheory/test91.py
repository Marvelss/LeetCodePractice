"""
@Author : SakuraFox
@Time: 2024-10-31 13:45
@File : test91.py
@Description : 417. 太平洋大西洋水流问题

思路：两洋同时访问
小技巧：利用两个visited标记，都标记过的表明都能踩到两洋
"""


class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(self, grid, visited, x, y):
        if visited[x][y]:
            return
        visited[x][y] = True
        for dx, dy in self.dirs:
            nextX, nextY = x + dx, y + dy
            if nextX < 0 or nextY < 0 or nextX >= len(grid) or nextY >= len(grid[0]):
                continue
            if grid[nextX][nextY] < grid[x][y]:
                continue
            self.dfs(grid, visited, nextX, nextY)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 是否访问到两个洋
        m, n = len(heights), len(heights[0])
        visitedP = [[False] * n for _ in range(m)]
        visitedO = [[False] * n for _ in range(m)]
        res = []
        for i in range(m):
            self.dfs(heights, visitedP, i, 0)
            self.dfs(heights, visitedP, i, n - 1)

        for i in range(n):
            self.dfs(heights, visitedP, 0, i)
            self.dfs(heights, visitedP, m - 1, i)

        for i in range(m):
            for j in range(n):
                if visitedO[i][j] and visitedP[i][j]:
                    res.append([i,j])
        return res
