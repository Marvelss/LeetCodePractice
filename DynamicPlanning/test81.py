"""
@Author : SakuraFox
@Time: 2024-10-13 19:14
@File : test81.py
@Description : 377. 组合总和 Ⅳ
要点:
组合问题--->先遍历背包,在遍历物品

"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i - nums[j]]
        return dp[target]

