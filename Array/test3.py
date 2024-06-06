"""
@Author : SakuraFox
@Time: 2024-06-06 19:40
@File : test3.py
@Description : 59.螺旋矩阵II(抄代码)
关键:
1.左闭右开循环填充
2.外圈为n整除2,内圈为四个方向依次填充(X,Y下标的变化),
注意:
若为奇数填充中间值
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startX, startY = 0, 0
        loop, mid = n // 2, n // 2
        count = 1
        for offset in range(1, loop + 1):  # 循环层数
            for i in range(startY, n - offset):  # 左闭右开,从左至右
                nums[startX][i] = count
                count += 1
            for i in range(startX, n - offset):  # 从上到下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, startY, -1):  # 从右到左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startX, -1):  # 从下到上
                nums[i][startY] = count
                count += 1
            # 更新起始点,以进入下一轮循环
            startX += 1
            startY += 1
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums
