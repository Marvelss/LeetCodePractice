"""
@Author : SakuraFox
@Time: 2024-12-11 18:07
@File : review46.py
@Description : 347.前 K 个高频元素(思路抄)
思路：
1.频率计算--->字典
2.频率排序--->引入小顶堆(堆顶为最小元素)
3.取前k个高频元素--->倒叙取元素
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1.频率计算
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        # 2.频率排序
        pri_que = []
        # 引入小顶堆
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        # 3.取前k个高频元素
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result


Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
