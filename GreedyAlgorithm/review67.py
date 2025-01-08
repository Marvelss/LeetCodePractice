"""
@Author : SakuraFox
@Time: 2025-01-08 8:47
@File : review67.py
@Description : 53. 最大子数组和-R1

思路：贪心算法：
局部最优：子字符串和>=0
注意点：
1.测试用例[4,-3,1]
虽然[4,-3]大于0，可继续加；但[4,-3,1]还是[4]大，所以应该取[4]
对应的处理：if count>maxNum:maxNum=count
2.若子字符串和，更新子字符串初始位置：if count<=0:count=0
3.其他编码上的思路优化，可使用count+=数字，代替数组引入，参考以下代码1和2比对


"""
from typing import List

"""
代码1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf') 
        count = 0
        for num in nums:
            count = num + count
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result
        
        
代码2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArr = [nums[0]]
        maxRes = nums[0]
        # j = 0
        for i in range(1, len(nums)):
            if nums[i] + sum(subArr) > 0:
                subArr.append(nums[i])
            else:
                if maxRes < sum(subArr):
                    # j = i
                    subArr = []
                    maxRes = sum(subArr)
        maxRes = sum(subArr)
        print(subArr)
        return maxRes      
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # j = 0
        maxNum = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > maxNum:
                maxNum = count
            if count <= 0:
                count = 0
        return maxNum


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
