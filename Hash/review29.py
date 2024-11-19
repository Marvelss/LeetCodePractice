"""
@Author : SakuraFox
@Time: 2024-11-19 9:44
@File : review29.py
@Description : 349. 两个数组的交集
思路：
将其中一个转为哈希表，然后通过另一数组访问判定存在，并set()去重
小技巧：
if n in table:通过tabel的键来判定n是否在其中，所以table[num] = 0
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, table = set(), {}
        for num in nums1:
            table[num] = 0
        for n in nums2:
            if n in table:
                res.add(n)
        return list(res)
