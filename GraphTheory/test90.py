"""
@Author : SakuraFox
@Time: 2024-10-30 12:18
@File : test90.py
@Description : 130. 被围绕的区域
思路：与1020. 飞地的数量思路一致，先遍历周围一圈以标记访问，然后遍历整体把无标记的'O'赋值为X
"""


class Solution:
    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def dfs(self, gridT, visitedT, x, y):
        visitedT[x][y] = True
        for dx, dy in self.dirs:
            nextX, nextY = x + dx, y + dy
            if nextX < 0 or nextY < 0 or nextX >= len(gridT) or nextY >= len(gridT[0]):
                continue
            if not visitedT[nextX][nextY] and gridT[nextX][nextY] == 'O':
                self.dfs(gridT, visitedT, nextX, nextY)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                self.dfs(board, visited, i, 0)
            if board[i][n - 1] == 'O' and not visited[i][n - 1]:
                self.dfs(board, visited, i, n - 1)
        for j in range(n):
            if board[0][j] == 'O' and not visited[0][j]:
                self.dfs(board, visited, 0, j)
            if board[m - 1][j] == 'O' and not visited[m - 1][j]:
                self.dfs(board, visited, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
