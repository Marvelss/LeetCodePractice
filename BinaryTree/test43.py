"""
@Author : SakuraFox
@Time: 2024-04-12 15:11
@File : test43.py
@Description : 700.二叉搜索树中的搜索
二叉搜索树根普通二叉树遍历区别在于,
搜索树根据输入值与节点值大小比较,直接递归另一边节点
if root.val < val:result = self.searchBST(root.right, val)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result = None
        if not root:
            return None
        if root.val == val:
            return root
        if root.val < val:
            result = self.searchBST(root.right, val)
        if root.val > val:
            result = self.searchBST(root.left, val)
        return result
