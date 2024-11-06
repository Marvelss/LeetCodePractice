"""
@Author : SakuraFox
@Time: 2024-11-05 19:38
@File : review20.py
@Description : 209.长度最小的子数组-R2(没完全做出来，思路代码参考)
滑动窗口三要素:
1.窗口内的内容-题目所需结果
2.滑动窗口起始位置-当窗口元素sum大于target，则往前移动
3.滑动窗口结束位置-遍历数组的指针

自己版本与正确版本区别： sumR -= nums[left]
自己版本：窗口移动时需要减去左指针的值
"""
from typing import List


class Solution:
    # 自己版本,代码通过部分结果
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int:
        slow = 0
        sumR = 0
        res = []
        while slow < len(nums):
            for i in range(slow, len(nums)):
                sumR += nums[i]
                if sumR > target:
                    sumR = 0
                    break
                if sumR == target:
                    res.append(i - slow)
                    sumR = 0
                    break
            if slow == 0:
                return 0
            slow += 1
        return min(res)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sumR = 0
        min_length = float('inf')
        while right < len(nums):
            sumR += nums[right]
            while sumR >= target:
                min_length = min(min_length, right - left + 1)
                sumR -= nums[left]
                left += 1
            right += 1
        return min_length if min_length != float('inf') else 0


Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
