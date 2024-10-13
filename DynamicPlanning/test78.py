"""
@Author : SakuraFox
@Time: 2024-09-29 20:02
@File : test78.py
@Description : 494.目标和(抄难)
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum =  sum(nums)

        if (target + total_sum) % 2 == 1 or abs(target) > sum(nums):
            return 0
        resultT = (target +total_sum) // 2
        dp = [[0] * (resultT + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1,len(nums)+1):
            for j in range(resultT+1):
                dp[i][j] = dp[i - 1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] +=dp[i - 1][j - nums[i-1]]
        return dp[len(nums)][resultT]
