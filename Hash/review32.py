"""
@Author : SakuraFox
@Time: 2024-11-22 13:39
@File : review32.py
@Description : 454. 四数相加 II-R1
思路：
1.将四个数组化简为两个数组，与两数之和解法类似
2.字典内存放内容，key：两数相加元素；value：出现次数
"""


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        table, count = {}, 0
        for a in nums1:
            for b in nums2:
                if a+b in table:
                    table[a + b] += 1
                else:
                    table[a + b] = 1
        for c in nums3:
            for d in nums4:
                another = 0 - c - d
                if another in table:
                    count += table[another]
        return count
