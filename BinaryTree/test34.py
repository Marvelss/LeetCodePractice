"""
@Author : SakuraFox
@Time: 2024-03-14 21:42
@File : test34.py
@Description: 222. 完全二叉树的节点个数
凭感觉写的第一遍就对了,但不理解代码具体如何运行??
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def count(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        right = self.count(node.right)
        left = self.count(node.left)
        print(right)
        print(left)
        print('===============')
        return 1 + left + right

    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = self.count(root)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def test_countNodes(self):
        # Create a binary tree with 3 nodes
        # 1
        # /
        # 2 3
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        solution = Solution()
        self.assertEqual(solution.countNodes(root), 3)
# Create a binary tree with 7 nodes
#    1
#   / \
#  2   3
# / \ / \
# 4 5 6 7
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        solution = Solution()
        self.assertEqual(solution.countNodes(root), 7)