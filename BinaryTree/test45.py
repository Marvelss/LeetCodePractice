"""
@Author : SakuraFox
@Time: 2024-04-16 18:31
@File : test45.py
@Description : 530. 二叉搜索树的最小绝对差
复习了昨天的二叉搜索树转换数组
但对求数组的最小绝对差值不太熟练
思路：遍历时前一个前=减后一个,同时跟原来差值比较取最小
注意：result = float('inf') # 表示正无穷大
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nodeList = []

    def travel(self, node: Optional[TreeNode]):
        # 初始条件
        if not node:
            return
        self.travel(node.left)
        self.nodeList.append(node.val)
        self.travel(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 转化数组
        self.travel(root)
        # 初始条件
        if len(self.nodeList) < 2:
            return 0
        result = float('inf')

        for j in range(1, len(self.nodeList)):
            result = min(result, abs(self.nodeList[j] - self.nodeList[j - 1]))
        return result
