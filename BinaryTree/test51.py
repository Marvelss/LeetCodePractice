"""
@Author : SakuraFox
@Time: 2024-05-06 21:23
@File : test51.py
@Description: 669. 修剪二叉搜索树(抄)
2个关键点:
1.遍历节点,截取left和right范围内数值
2.修剪子节点(针对野节点)
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val > high:
            return self.trimBST(root.left, low, high)
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
