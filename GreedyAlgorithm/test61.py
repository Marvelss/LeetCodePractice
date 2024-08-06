"""
@Author : SakuraFox
@Time: 2024-07-25 20:43
@File : test61.py
@Description :860.柠檬水找零(思路抄)
思路:只有5、10、20三种情况一一分析
5:收取
10:-5,+10
20:①-5*3②-5 -10
"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            elif bill == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five = five - 3
            if five<0 or ten<0:
                return False
        return True
