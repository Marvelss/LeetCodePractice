"""
@Author : SakuraFox
@Time: 2024-11-05 19:03
@File : review19.py
@Description : 977.有序数组的平方-R1

思路：双指针，前指头，后指尾
注意:存放结果顺序为倒叙，因为原数组为非递减，最后一个元素的平方一定是最大，而第一个元素的平方不一定最小
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        left, right, k = 0, len(nums) - 1, len(nums) - 1
        while left <= right:
            if nums[left] * nums[left] <= nums[right] * nums[right]:
                res[k] = nums[left] * nums[left]
                k -= 1
                left += 1
            else:
                res[k] = nums[right] * nums[right]
                k -= 1
                right -= 1
        return res
