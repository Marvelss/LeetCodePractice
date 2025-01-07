"""
@Author : SakuraFox
@Time: 2025-01-07 9:42
@File : review66.py
@Description : 376. 摆动序列

思路1：29 / 32 个通过的测试用例(结果少1)
1.判断+，-摆动
2.若同号，则取差值最小元素

思路2:贪心算法
考虑三种情况
1.平坡 (prevDF = 0,curDF<0) or (prevDF = 0,curDF>0)
2.单调平坡 (prevDF >= 0,curDF<0) or (prevDF <= 0,curDF>0)时更新curDF
3.首位两端 不遍历最后一个元素，res初始为1


"""
from typing import List

"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        curDiff = 0
        preDiff = 0
        result = 1
        for i in range(len(nums) - 1):
            # 后值减前值
            curDiff = nums[i + 1] - nums[i]

            if (curDiff < 0 and preDiff >= 0) or (curDiff > 0 and preDiff <= 0):
                result += 1
                preDiff = curDiff
        return result
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        isRepetition = False
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1
        resList = [nums[0], nums[1]]
        minDV = resList[1] - resList[0]
        for i in range(2, len(nums)):
            prevDV = nums[i - 2] - nums[i - 1]
            curDV = nums[i - 1] - nums[i]
            # 若异号，则添加元素
            if prevDV > 0 > curDV or prevDV < 0 < curDV:
                resList.append(nums[i])
            else:
                # 若同号，则取差值最小元素
                if minDV > curDV:
                    # print(nums[i - 1])
                    resList.pop()
                    resList.append(nums[i])
                    # print(f'移除元素:{nums[i - 1]}  \n添加元素{nums[i]}')
                    minDV = curDV
                # 解决[0,0,0]问题
                elif curDV == 0 and minDV == curDV:
                    isRepetition = True
                if minDV != curDV:
                    isRepetition = False

        return len(resList) if not isRepetition else len(resList) - 1

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        prevDV = 0
        curDF = 0
        res = 1
        for i in range(len(nums) - 1):
            curDF = nums[i + 1] - nums[i]
            if prevDV >= 0 > curDF or prevDV <= 0 < curDF:
                res += 1
                prevDV = curDF
        return res
