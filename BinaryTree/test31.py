"""
@Author : SakuraFox
@Time: 2024-02-29 19:27
@File : test31.py
@Description: 101. 对称二叉树
1.确定递归三步走
2.判断左右节点存在空值的不对称条件
3.判断左右节点不相等条件(外侧与内侧节点值都相等)
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 遍历左右节点如果不相等返回False
        if not root:
            return True
        return self.compare(root.left, root.right)
