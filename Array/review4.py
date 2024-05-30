"""
@Author : SakuraFox
@Time: 2024-05-30 20:42
@File : review4.py
@Description : 977. 有序数组的平方-复习-1
小技巧:
1.结果数组从末尾开始复赋值
注意
1.while left <= right:边界值'='
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, t = 0, len(nums) - 1, len(nums) - 1
        result = [float('inf')] * len(nums)
        while left <= right:
            l = nums[left] * nums[left]
            r = nums[right] * nums[right]
            if l > r:
                result[t] = l
                left += 1
            else:
                result[t] = r
                right -= 1
            t -= 1
        return result
