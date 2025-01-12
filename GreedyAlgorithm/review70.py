"""
@Author : SakuraFox
@Time: 2025-01-11 14:39
@File : review70.py
@Description : 分发饼干-跳跃游戏-周复习
"""
from typing import List


# 455.分发饼干
# 思路：
# 局部最优：大尺寸饼干-->大胃口小孩
# 关键点：使用尺寸中的下标自减实现单层for循环
# 注意点：倒序遍历
def findContentChildren1(self, g: List[int], s: List[int]) -> int:
    s.sort()
    g.sort()
    j = len(s) - 1
    res = 0
    for i in range(len(g) - 1, -1, -1):
        if j >= 0 and s[j] >= g[i]:
            res += 1
            j -= 1
    return res


# 376. 摆动序列
# 思路：
# 局部最优：删除单调坡度上的节点
# 考虑三种情况
# 1.平坡（prevDF=O,curDF>0 OR prevDF=0,curDF<0）
# 2.首位两端（针对prevDF=0，curDF>0情况默认最右面有一个峰值，即初始峰值为1）
# 3.单调平坡（针对该情况，坡度变化时才更新prevDF）
def wiggleMaxLength(self, nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    prevDF, curDF = 0, 0
    res = 1
    for i in range(len(nums) - 1):
        curDF = nums[i + 1] - nums[i]
        if prevDF >= 0 > curDF or prevDF <= 0 < curDF:
            res += 1
            prevDF = curDF
    return res


# 53. 最大子数组和
# 思路：局部最优-子字符串和>=0
def maxSubArray(self, nums: List[int]) -> int:
    maxNum = float('-inf')
    count = 0
    for i in range(len(nums)):
        count += nums[i]
        if count > maxNum:
            maxNum = count
        if count <= 0:
            count = 0
    return maxNum


# 122. 买卖股票的最佳时机 II
# 思路：局部最优-只收集每天正利润
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - - prices[i - 1]
    return profit


# 55. 跳跃游戏
# 思路：局部最优-移动下标每次取最大跳跃步数（取最大覆盖范围）

def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    cover, i = 0, 0
    while i <= cover:
        cover = max(cover, i + nums[i])
        if cover >= len(nums) - 1:
            return True
        i += 1
    return False
