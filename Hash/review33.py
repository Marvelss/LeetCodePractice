"""
@Author : SakuraFox
@Time: 2024-11-23 16:11
@File : review33.py
@Description : 第15题. 三数之和-R1
思路：双指针法，固定正常遍历输入下标i为a；三数之和正负性,
同时动b以(i+1)、c(以len(nums)-1)
缩小b、c范围
关键：结果去重
a:if i > 0 and nums[i] == nums[i - 1]:continue
b:while right > left and nums[left] == nums[left + 1]:left += 1
c:while right > left and nums[right] == nums[right - 1]:right -= 1

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return result

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while right > left:
                # 三数之和
                sumNum = nums[i] + nums[left] + nums[right]
                if sumNum < 0:
                    left += 1
                elif sumNum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result