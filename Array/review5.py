"""
@Author : SakuraFox
@Time: 2024-06-04 21:20
@File : review5.py
@Description : 209.长度最小的子数组-复习-1(抄了下,
只记得是滑动窗口，而忘记具体如何展示)
思路：
1.滑动窗口内数值是长度最小数组
2.滑动窗口起始位置构根据cum >= target？移动
3.滑动窗口截至位置为遍历nums数组索引
注意：
1.当窗口内超过目标值时,cum减去下标left元素,cum -= nums[left]
2.写while循环时理清终止条件,并记得索引累加
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        left, right = 0, 0
        cum = 0
        min_len = float('inf')
        while right < l:
            cum += nums[right]
            while cum >= target:
                min_len = min(min_len, right - left + 1)
                cum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0
