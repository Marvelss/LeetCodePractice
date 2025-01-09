"""
@Author : SakuraFox
@Time: 2025-01-09 15:25
@File : review68.py
@Description : 122. 买卖股票的最佳时机 II-R1(思路抄)

思路:每天买入并卖出,利润分解
例如第0天买入,第3天卖出:profit=prices[3] - prices[0]
等价于profit=(prices[3]-prices[2]) + (prices[2]-prices[1])+ (prices[1]-prices[0])
所以只计算利润为正即可
局部最优：收集每天的正利润，全局最优：求得最大利润

注意:可以一天先卖出,后再买入


"""
from typing import List

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 1
        while i < len(prices):
            result += max(prices[i] - prices[i-1], 0)
            i += 1
        return result

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


Solution().maxProfit([1, 2])
