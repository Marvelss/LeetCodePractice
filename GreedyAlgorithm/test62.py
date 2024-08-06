"""
@Author : SakuraFox
@Time: 2024-08-06 16:03
@File : test62.py
@Description : 406.根据身高重建队列(抄)
思路:从两个维度考虑，先确定一个维度，然后对另一个维度考虑贪心思想
按照身高从小到大排序,然后再按照前人个数插入(刚好数量从0开始,与下标一致)
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for temp in people:
            result.insert(temp[1], temp)
        return result
