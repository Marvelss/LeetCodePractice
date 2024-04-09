"""
@Author : SakuraFox
@Time: 2024-04-09 21:33
@File : test41.py
@Description : 654.最大二叉树
逻辑：
1.以最大值作为根节点
2.根据最大值下标获取左右数组
3.递归循环
注意:
if rootIds > 0 和  if rootIds < len(nums) - 1条件以及初始空值
感想:
总体来说与昨天的617. 从中序与后序遍历序列构造二叉树思路类似
"""
from functools import reduce
from typing import List, Optional

import numpy as np


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return TreeNode()
        max_value = 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
        root = TreeNode(val=max_value)
        rootIds = nums.index(max_value)
        if rootIds > 0:
            leftList = nums[:rootIds]
            root.left = self.constructMaximumBinaryTree(leftList)

        if rootIds < len(nums) - 1:
            rightList = nums[rootIds + 1:]
            root.right = self.constructMaximumBinaryTree(rightList)
        return root
