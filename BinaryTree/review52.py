"""
@Author : SakuraFox
@Time: 2024-12-18 16:11
@File : review52.py
@Description : 226.翻转二叉树-R1(代码简单，但思路想不到)
思路：
递归遍历的同时翻转节点
root.left, root.right = root.right, root.left
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
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
