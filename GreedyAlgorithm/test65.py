"""
@Author : SakuraFox
@Time: 2024-08-12 21:39
@File : test65.py
@Description : 56. 合并区间(软磨硬泡出结果)
思路与无重叠区间类似,多了一步合并区间的操作
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        if len(intervals) == 1:
            return intervals
        result = []
        i = 1
        flag = True
        while i < len(intervals):
            if intervals[i - 1][1] >= intervals[i][0]:
                # result.append([intervals[i-1][0],intervals[i][1]])
                intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i - 1][0])
                flag = False
            if flag:
                result.append(intervals[i - 1])
            flag = True
            i += 1
        result.append(intervals[i - 1])
        return result
