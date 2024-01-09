"""
@Author  : SakuraFox
@Time    : 2024-01-09 23:06
@File    : test29.py
@Description : 102.二叉树的层序遍历
不太明白,初步模仿代码
"""
import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queen = collections.deque([root])
        result = []

        while queen:
            sub_result = []
            for _ in range(len(queen)):
                node = queen.popleft()
                sub_result.append(node.val)
                if node.left:
                    sub_result.append(node.left)
                if node.right:
                    sub_result.append(node.right)
            result.append(sub_result)
        return result
