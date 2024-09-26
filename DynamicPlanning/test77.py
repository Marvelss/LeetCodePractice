"""
@Author : SakuraFox
@Time: 2024-09-26 18:33
@File : test77.py
@Description : 1049.最后一块石头的重量II(抄)
理解转为0-1背包问题关键
dp[target]:target的背包所能背的最大重量,sum-dp[target]则是另一堆石头重量(分成重量相同的两堆)
sum-dp[target] - dp[target] 则是所能得到的最小石头重量,也就是题意
动归步骤与416. 分割等和子集类似
"""


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        count = sum(stones)
        target = count // 2
        dp = [0] * (target + 1)
        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
            print(dp)
        return count - dp[target] - dp[target]
