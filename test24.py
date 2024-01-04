"""
@Author  : SakuraFox
@Time    : 2024-01-02 21:42
@File    : test24.py
@Description : 94. 二叉树的中序遍历
递归思想确定三要素：
1.需要递归的函数内的参数和返回值,前序遍历结果(左、中、右)
2.终止条件
3.单层递归的逻辑
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left +[root.val] +right
