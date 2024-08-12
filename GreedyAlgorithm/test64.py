"""
@Author : SakuraFox
@Time: 2024-08-12 19:45
@File : test64.py
@Description : 435. 无重叠区间
思路和用最少数量的箭引爆气球类似但又是这个点卡住，
伴随数组遍历，右边通过取前后元素的最小值再动
intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = 0
        i = 1
        while i < len(intervals):
            if intervals[i - 1][1] > intervals[i][0]:
                result += 1
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
            i += 1
        print(intervals)
        return result


Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]])
