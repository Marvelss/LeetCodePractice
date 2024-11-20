"""
@Author : SakuraFox
@Time: 2024-11-20 13:10
@File : review30.py
@Description : 第202题. 快乐数-R2
思路：逐步迭代n，直到n出现在哈希表中，注意取整数每个位上的数的代码
小技巧：
1.取整数每个位上的数
while num:
    num, r = divmod(num, 10)
2.优化
while self.calNum(n) != 1:不需要重复判定，当n出现重复出现在字典中，停止循环；
另一种停止循环的情况是1，10，100的值仍然是1，所以重复出现且结果为1时，则为True
"""


class Solution:
    def calNum(self, num: int) -> int:
        new_num = 0
        while num:
            num, r = divmod(num, 10)
            new_num += r ** 2
        return new_num

    def isHappy(self, n: int) -> bool:
        table = set()
        if n == 1:
            return True
        while self.calNum(n) != 1:
            # 计算新的数
            if n in table:
                return False
            else:
                table.add(n)
                n = self.calNum(n)
        return True


Solution().isHappy(2)
# table = set()
# table.add(1)
# table.add(2)
# table.add(3)
# print(4 in table)
# print(2 % 10)
# print(20 % 10)
