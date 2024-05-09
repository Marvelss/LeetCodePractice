"""
@Author : SakuraFox
@Time: 2024-05-09 21:39
@File : test53.py
@Description : 538.把二叉搜索树转换为累加树(抄)
思路：
有序数组[2, 5, 13],求累加数组，也就是[20, 18, 13],
当二叉树的遍历顺序为右中左,与上一致
工具：cur+右中左遍历
注意:不接返回值
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cur = 0

    def traversal(self, node: Optional[TreeNode]):
        if node is None:
            return None
        self.convertBST(node.right)
        node.val += self.cur
        self.cur = node.val
        self.convertBST(node.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traversal(root)
        return root
