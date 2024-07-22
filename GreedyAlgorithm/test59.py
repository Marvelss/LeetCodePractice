"""
@Author : SakuraFox
@Time: 2024-07-22 19:32
@File : test59.py
@Description : 1005.K次取反后最大化的数组和(完整自想)
思路:取数组最小元素(正数时取最小,负数时取绝对值最大)取反
还有另一种代码编写思路:先排序,然后依次取反,最后k有余数时绝对值最小值取反
"""
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            nums[nums.index(min(nums))] = -min(nums)
        return sum(nums)


Solution().largestSumAfterKNegations([2,-3,-1,5,-4],2)