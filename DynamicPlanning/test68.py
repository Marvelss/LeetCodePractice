"""
@Author : SakuraFox
@Time: 2024-08-19 20:27
@File : test68.py
@Description : 509. 斐波那契数
思路:
1.确认dp数组及下标 i:dp[i]
2.确定递推公式
3.dp初始化
4.确定遍历顺序
5.举例演绎dp
小技巧:可用递归法
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # 递归写法
    def fib1(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
