"""
@Author : SakuraFox
@Time: 2024-03-04 20:49
@File : test32.py
@Description: 104.二叉树的最大深度
注意最大深度和高度概念,(根节点)的高度就是二叉树的最大深度
操作：遍历同时加一步计数操作
depth = 1 + max(ld, rd)这一步+1是因为算上当前中间节点不太清楚
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        ld = self.getDepth(node.left)
        rd = self.getDepth(node.right)
        depth = 1 + max(ld, rd)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
