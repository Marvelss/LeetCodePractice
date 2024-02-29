"""
@Author  : SakuraFox
@Time    : 2024-01-23 9:10
@File    : test30.py
@Description : 226.翻转二叉树
(递归法前序遍历)从整体到局部交互左右节点
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
