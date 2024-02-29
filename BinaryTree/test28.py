"""
@Author  : SakuraFox
@Time    : 2024-01-07 22:23
@File    : test28.py
@Description : 145. 二叉树的后序遍历(迭代法)
注意:需要判断当子节点不为空时,才放入栈
将数组反转result[::-1]
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
        stack = [root]
        result = []
        if root is None:
            return []
        while stack:
            node = stack.pop()
            node_left = node.left
            node_right = node.right
            result.append(node.val)
            if node_left:
                stack.append(node_left)
            if node_right:
                stack.append(node_right)
        return result[::-1]
