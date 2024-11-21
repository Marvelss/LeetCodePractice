"""
@Author : SakuraFox
@Time: 2024-11-21 16:18
@File : review31.py
@Description : 1. 两数之和-R2
思路：三种解法
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解法一：暴力解法
        :param nums:
        :param target:
        :return:
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解法二：
        1.nums存为set()，遍历查找anotherNum = target - nums[i]是否存在set()内
        2.解决[3,3],target=6这样的情况，重复元素
        :param nums:
        :param target:
        :return:
        """
        table = set(nums)
        for i in range(len(nums)):
            anotherNum = target - nums[i]
            if anotherNum in table and anotherNum != nums[i]:
                return [i, nums.index(anotherNum)]
            elif anotherNum in table and anotherNum == nums[i]:
                first_index = nums.index(anotherNum)
                if first_index != i:
                    return [i, first_index]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
           解法三：
           1.放置一个seen为set()，遍历并查找anotherNum = target - nums[i]是否在seen中，
           好处：包含[3,3]情况
           :param nums:
           :param target:
           :return:
       """
        seen = set()
        for i in range(len(nums)):
            anotherNum = target - nums[i]
            if anotherNum in seen:
                return [i, nums.index(anotherNum)]
            seen.add(nums[i])


print([3, 3].index(3))
