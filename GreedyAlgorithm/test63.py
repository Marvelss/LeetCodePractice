"""
@Author : SakuraFox
@Time: 2024-08-08 20:39
@File : test63.py
@Description : 452. 用最少数量的箭引爆气球
思路与实际一致:先对左元素排序,然后根据右元素是否points[i - 1][1] < points[i][0]
但缺了遍历的同时实时更新最小元素:
points[i][1] = min(points[i][1], points[i - 1][1])
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        print(points)
        result = 1
        for i in range(1, len(points)):
            if points[i - 1][1] < points[i][0]:
                result += 1
            else:
                points[i][1] = min(points[i][1], points[i - 1][1])
        return result


Solution().findMinArrowShots(
    [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
