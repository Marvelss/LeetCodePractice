# 1. 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in res:
                return [res[another_num], index]
            else:
                res[num] = index
        return []
