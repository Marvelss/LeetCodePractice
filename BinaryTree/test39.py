"""
@Author : SakuraFox
@Time: 2024-03-27 18:38
@File : test39.py
@Description: 112. 路径总和
跟着代码抄了一遍
其中思路在二叉树的所有路径的回溯基础上添加了一步数值操作
数值计算逻辑代码实现不太明白
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, count):
        if not node.left and not node.right and count == 0:
            return True
        if not node.left and not node.right:
            return False
        if node.left:
            count -= node.left.val
            if self.traversal(node.left, count):
                return True
            count += node.left.val

        if node.right:
            count -= node.right.val
            if self.traversal(node.right, count):
                return True
            count += node.right.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.traversal(root, targetSum)
