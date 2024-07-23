"""
@Author : SakuraFox
@Time: 2024-07-23 19:02
@File : test60.py
@Description : 134. 加油站(抄)
思路:curRest += gas[i] - cost[i]不小于0则可以作为起点
注意：当curRest += gas[i] - cost[i] ,curRest<0时需要重新归零
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalRest, curRest, result = 0, 0, 0
        for i in range(len(gas)):
            curRest += gas[i] - cost[i]
            totalRest += gas[i] - cost[i]
            if curRest < 0:
                result = i + 1
                curRest = 0
        if totalRest<0:
            return -1
        return result

