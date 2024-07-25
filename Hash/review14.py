"""
@Author : SakuraFox
@Time: 2024-07-25 20:48
@File : review14.py
@Description : 202. 快乐数(思路抄)
思路:
1.取各位上单数
2.判断和情况:1/非1/是否陷入重复循环数值
"""


class Solution:
    # 取数值各个位上的单数之和
    def getSum(self, n):
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num

    def isHappy(self, n: int) -> bool:
        result = set()
        while 1:
            n = self.getSum(n)
            if n in result:
                return False
            elif n == 1:
                return True
            else:
                result.add(n)

