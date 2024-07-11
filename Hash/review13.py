"""
@Author : SakuraFox
@Time: 2024-07-11 19:43
@File : review13.py
@Description : 349. 两个数组的交集-review-1
方法:1.字典和数组配合2.暴力解法
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 字典和数组配合
        table = {}
        for i in nums1:
            table[i] = table.get(i, 0) + 1
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
        return list(res)
        # 暴力解法
        # res = []
        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             res.append(i)
        # return list(set(res))
