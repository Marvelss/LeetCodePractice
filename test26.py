"""
@Author  : SakuraFox
@Time    : 2024-01-03 23:12
@File    : test26.py
@Description : 144. 二叉树的前序遍历(迭代法)

迭代法:将所有结果保存在数组中,考虑每次循环内操作的节点
1.区分节点和节点值的看法
2.注意:将结果压入栈时,先压右节点
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        if root is None:
            return []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
