"""
@Author : SakuraFox
@Time: 2024-03-18 20:56
@File : test35.py
@Description: 110.平衡二叉树
条件：abs(left - right) > 1
代入测试用例逐步走代码后感觉理解更深了
递归就是一条路挖到底,结束了才跳出这条路
也理解return max(left, right) + 1原来已经是路全走完最终的结果
"""
import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

