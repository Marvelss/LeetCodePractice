"""
@Author : SakuraFox
@Time: 2024-07-15 18:56
@File : test56.py
@Description : 376. 摆动序列
技巧:
1.局部最优:连续和不为负数
2.遇到负数重新计算和(赋值0)
3.一个动态算连续和,一个用来存结果,从而比大小
注意:result初始值为无穷小,不然负数不过关
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            count = num + count
            if count > result:
                result = count
            if count < 0:
                count = 0
                result = count
        return result


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
