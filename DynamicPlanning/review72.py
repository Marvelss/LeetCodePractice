"""
@Author : SakuraFox
@Time: 2025-01-14 9:04
@File : review72.py
@Description : 70. 爬楼梯-R1

1.n:阶梯；dp[n]:爬n阶到楼顶的方法数量
2.DP[N] = DP[N-1] + DP[N-2]
3.DP[1]=1
4.+
5.举例
"""

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
    
        result = [0] * (n + 1)
        result[1],result[2]=1,2
        for i in range(3, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
