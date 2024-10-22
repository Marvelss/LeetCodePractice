"""
@Author : SakuraFox
@Time: 2024-10-22 16:18
@File : test86.py
@Description : 99. 岛屿数量

方法：深度搜索
关键：同化
注意点：周围四点坐标
技巧：visited减少运行次数
"""

# 上下左右周围网点
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(gridT, visitedT, x, y):
    for o, p in direction:
        next_x = x + o
        next_y = y + p
        # 判断点越界情况
        if next_x < 0 or next_y < 0 or next_x >= len(gridT) or next_y >= len(gridT[0]):
            continue
        if not visitedT[next_x][next_y] and gridT[next_x][next_y] == 1:
            visitedT[next_x][next_y] = True
            dfs(gridT, visitedT, next_x, next_y)


if __name__ == '__main__':
    n, m = map(int, input().split())

    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

    # 是否已访问
    visited = [[False] * m for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(m):
            # 判断岛屿和是否已访问
            if grid[i][j] == 1 and not visited[i][j]:
                # 同化
                result += 1
                visited[i][j] = True
                dfs(grid, visited, i, j)
    print(result)