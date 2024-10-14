"""
@Author : SakuraFox
@Time: 2024-10-14 15:59
@File : test82.py
@Description : 57. 爬楼梯
要点:
1.m代表物品,n代表背包
2.排列问题-->先遍历背包,后遍历物品
3.公式:dp[i]+=dp[i-j]
"""


def climbing_stairs(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(m + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[n]


if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    print(climbing_stairs(n, m))
