"""
@Author : SakuraFox
@Time: 2024-05-23 21:33
@File : review1.py
@Description : 704. 二分查找-复习-1
注意：
1.定义 target 是在一个在左闭右闭的区间
2.while (left <= right) 要使用 <= ,因为left == right是有意义的
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return -1
