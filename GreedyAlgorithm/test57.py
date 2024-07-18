"""
@Author : SakuraFox
@Time: 2024-07-18 18:55
@File : test57.py
@Description : 122. 买卖股票的最佳时机 II
思路:直接以每天为单位根据前天买入今天卖出规律依次计算利润
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 1
        while i < len(prices):
            result += max(prices[i] - prices[i-1], 0)
            i += 1
        return result
