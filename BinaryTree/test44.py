"""
@Author : SakuraFox
@Time: 2024-04-15 21:44
@File : test44.py
@Description : 98.验证二叉搜索树
通过中序遍历转为数组，使用递增的特性判断是否为二叉搜索树（思路抄了一遍）
主要条件:self.var[i] <= self.var[i - 1]
注意:遍历时下标从1开始
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
        self.var = []

    # 中序遍历转为数组
    def traversal(self, root: Optional[TreeNode]):
        # 初始判断
        if not root:
            return True
        self.traversal(root.left)
        self.var.append(root.val)
        self.traversal(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.traversal(root)
        # 注意这里索引从1开始
        for i in range(1, len(self.var)):
            if self.var[i] <= self.var[i - 1]:
                return False
        return True
