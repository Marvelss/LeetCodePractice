"""
@Author : SakuraFox
@Time: 2024-04-11 22:35
@File : test42.py
@Description : 617.合并二叉树
核心问题:如何同时遍历两个二叉树?
解决:遍历2个二叉树与1个一样.同时传入两个二叉树,所以这两个二叉树的叶子节点位置一致,
只需要作两节点值相加操作即可.
小技巧:以第一个二叉树的节点作为模板叠加值,而不是创建第三个二叉树存储两节点相加后的值
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
