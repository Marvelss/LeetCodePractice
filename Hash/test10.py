# hash table
# 349. 两个数组的交集
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        # 转化成哈希表
        for n in nums1:
            table[n] = table.get(n, 0) + 1
        res = set()
        # 用另一个数组去比对这个哈希表
        for n in nums2:
            if n in table:
                res.add(n)
                del table[n]
        print(res)
        print(list(res))
        return list(res)


nums1_1 = [1, 2, 2, 1]
nums2_1 = [2, 2]
solution = Solution()
result1 = solution.intersection(nums1_1, nums2_1)
