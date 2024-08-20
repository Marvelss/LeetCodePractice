"""
@Author : SakuraFox
@Time: 2024-08-20 19:01
@File : test69.py
@Description : 70. 爬楼梯(思路抄)
1.爬i层有dp[i]种方法(不确幸)
2.公式:dp[i]=dp[i-1]+dp[i-2](不确幸)
3.初始化OK
4.从前往后(不确幸)

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = [0] * (n + 1)
        result[1], result[2] = 1, 2
        for i in range(3, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]
