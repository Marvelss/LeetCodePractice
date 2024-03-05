"""
@Author : SakuraFox
@Time: 2024-03-05 21:37
@File : test33.py
@Description: 111. 二叉树的最小深度
叶子节点，左右孩子都为空的节点才是叶子节点
如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度
反之，左不空， 右空，左+1
左不空，右不空，1+min(左，右)
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
        if not node:
            return 0
        left = self.getDepth(node.left)
        right = self.getDepth(node.right)
        if node.left is None and node.right is not None:
            return 1 + right
        elif node.right is None and node.left is not None:
            return 1 + left
        return 1 + min(left, right)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
