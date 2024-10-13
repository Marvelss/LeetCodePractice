"""
@Author : SakuraFox
@Time: 2024-10-12 19:19
@File : test80.py
@Description : 518.零钱兑换II(抄,演绎了下稍明白些)

"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]
