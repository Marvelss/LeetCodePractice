"""
@Author  : SakuraFox
@Time    : 2024-01-02 21:42
@File    : test25.py
@Description : 145. 二叉树的后序遍历
递归思想确定三要素：
1.需要递归的函数内的参数和返回值,前序遍历结果(左、右、中)
2.终止条件
3.单层递归的逻辑
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]
