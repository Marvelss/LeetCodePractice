"""
@Author : SakuraFox
@Time: 2024-04-28 20:36
@File : test49.py
@Description: 701. 二叉搜索树中的插入操作(思路简单)
小技巧:递归函数添加返回值,用于将新节点插入父节点
root.left = self.insertIntoBST(root.left, val)
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
