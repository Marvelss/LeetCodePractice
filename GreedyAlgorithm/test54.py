"""
@Author : SakuraFox
@Time: 2024-05-27 21:30
@File : test54.py
@Description : 455. 分发饼干
思路:局部最优:大尺寸满足胃口;全局最优:尽可能满足越多数量的孩子
小技巧:两数组同时遍历,类似双指针
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count, index = 0, len(g) - 1
        g.sort()
        s.sort()

        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                count += 1
                index -= 1
        return count
