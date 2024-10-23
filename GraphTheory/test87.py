"""
@Author : SakuraFox
@Time: 2024-10-23 15:57
@File : test87.py
@Description : 99. 岛屿数量

与深度搜索相比，多了队列内容
方法：广度搜索
关键：同化、队列
注意点：周围四点坐标
技巧：visited减少运行次数
"""
import queue
from collections import deque


class Solution:
    def __init__(self):
        self.dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]  # 创建方向元素

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, visited, i, j)

        return res

    def bfs(self, grid, visited, x, y):
        que = deque()
        que.append((x, y))  # 放入第一个元素/起点
        visited[x][y] = True
        while que:
            curX, curY = que.popleft()
            for dx, dy in self.dir:
                nextCurX, nextCurY = curX + dx, curY + dy
                if nextCurX < 0 or nextCurX >= len(grid) or nextCurY < 0 or nextCurY >= len(grid[0]):
                    continue
                # print(nextCurX)
                # print('-----')
                # print(nextCurY)
                if not visited[nextCurX][nextCurY] and grid[nextCurX][nextCurY] == '1':
                    que.append((nextCurX, nextCurY))
                    visited[nextCurX][nextCurY] = True
