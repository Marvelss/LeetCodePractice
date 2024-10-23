"""
@Author : SakuraFox
@Time: 2024-10-18 18:51
@File : test85.py
@Description : 98. 所有可达路径(抄)
卡码网
邻接矩阵获取输入
"""


def dfs(graphT, x, nT, path, resultT):
    if x == nT:
        resultT.append(path.copy())
        return
    for i in range(1, nT + 1):
        if graphT[x][i] == 1:
            path.append(i)
            dfs(graphT, i, nT, path, resultT)
            path.pop()  # 回头


def start():
    # 邻接矩阵存放参数
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(n):
        s, t = map(int, input().split())
        graph[s][t] = 1

    # 初始化
    result = []
    dfs(graph, 1, n, [1], result)
    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str, path)))


if __name__ == '__main__':
    start()
