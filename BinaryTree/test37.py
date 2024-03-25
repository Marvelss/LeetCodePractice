"""
@Author : SakuraFox
@Time: 2024-03-25 21:34
@File : test37.py
@Description: 404.左叶子之和
注意左右节点都为空,根节点不为空返回0情况
再次明晰了一遍前序遍历流程,先遍历左侧所有子树,再遍历右侧所有
注意left = root.left.val与
right = self.sumOfLeftLeaves(root.right)的区别
因为条件是if not root.left and not root.right:return 0
所以最后一个右子叶right返回0
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            left = root.left.val
        right = self.sumOfLeftLeaves(root.right)
        return left + right
