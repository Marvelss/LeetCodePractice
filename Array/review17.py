"""
@Author : SakuraFox
@Time: 2024-11-04 18:44
@File : review17.py
@Description : 704. 二分查找-R2
中点选取：mid = (j + i) // 2与mid = i + (j - i) // 2区别
当i+j很大时可能导致数值溢出，而j-i可以避免潜在溢出
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (j + i) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
