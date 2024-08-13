"""
@Author : SakuraFox
@Time: 2024-08-13 18:50
@File : test66.py
@Description : 763. 划分字母区间(抄)
思路
1.先遍历字母记录每个元素出现的最远下标
2.若元素下标和传入字符串一样,则作为分割点,记录start和end为最终结果
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map1 = {}
        for index, value in enumerate(s):
            map1[value] = index
        count = []
        start, end = 0, 0
        for index, value in enumerate(s):
            # 遍历元素找到每个元素最远的值
            end = max(end, map1[value])
            if end == index:
                start = index + 1
                count.append(end - start)
        return count
