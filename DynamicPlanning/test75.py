"""
@Author : SakuraFox
@Time: 2024-09-23 22:01
@File : test75.py
@Description : 动态规划：01背包理论基础
解法一.二位数组
1.意义:i-物品;j-重量;dp[i][j]-最大价值
2.公式:dp[i][j]=max(dp[i-1][j],dp[j-weight[i]]+value[i])
解法二.一维滚动数组
1.意义:j-重量dp[j]-最大价值
2.公式:dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
"""


def wei_bag_problem1():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4
    # 二维数组
    dp = [[0] * (bagweight + 1) for _ in range(len(weight))]

    # 初始化
    for j in range(weight[0], bagweight + 1):
        dp[0][j] = value[0]

    # weight数组的大小就是物品个数
    for i in range(1, len(weight)):  # 遍历物品
        for j in range(bagweight + 1):  # 遍历背包容量
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[len(weight) - 1][bagweight]


# 一维数组解决背包问题
def wei_bag_problem2():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):
        for j in range(bagWeight, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]


if __name__ == "__main__":
    print(wei_bag_problem1())
    print(wei_bag_problem2())
