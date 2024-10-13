"""
@Author : SakuraFox
@Time: 2024-09-27 16:36
@File : review16.py
@Description : 0-1背包基本问题
"""


def bag01_one():
    # 输入
    weight, value = [2, 2, 3, 1, 5, 2], [2, 3, 1, 5, 4, 3]
    bagWeight = 6
    # 初始化
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):
        for j in range(bagWeight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    print(dp)
    return dp[bagWeight]


def bag01_two():
    # 输入
    weight, value = [2, 2, 3, 1, 5, 2], [2, 3, 1, 5, 4, 3]
    bagWeight = 6
    dp = [[0] * (bagWeight + 1) for _ in range(len(weight))]
    for i in range(len(weight)):
        for j in range(bagWeight):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i])

print(bag01_one())
