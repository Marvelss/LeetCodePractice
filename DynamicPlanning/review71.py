"""
@Author : SakuraFox
@Time: 2025-01-13 13:29
@File : review71.py
@Description : 509. 斐波那契数-R1
1.确定dp与下标含义-dp：前n项和；n：第n个数
2.递推公式-F(n) = F(n-1)+F(n-2)
3.dp初始化-dp[0]=0;dp[1]=1
4.遍历顺序-正向
5.举例推导公式
"""
"""
class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*(n+1)
        if n==0:
            return 0
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            dp[i] =dp[i-1]+dp[i-2]
        return dp[n] 

"""


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
