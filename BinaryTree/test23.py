"""
@Author  : SakuraFox
@Time    : 2024-01-02 21:42
@File    : test23.py
@Description : 144. 二叉树的前序遍历
递归思想确定三要素：
1.需要递归的函数内的参数和返回值,前序遍历结果(中、左、右)
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right


import unittest
from idlelib.tree import TreeNode


class TestSolution(unittest.TestCase):
    def test_preorderTraversal_empty_tree(self):
        sol = Solution()
        result = sol.preorderTraversal(None)
        self.assertEqual(result, [])

    def test_preorderTraversal_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        result = sol.preorderTraversal(root)
        self.assertEqual(result, [1])

    def test_preorderTraversal_full_tree(self):
        sol = Solution()
        # Construct a tree:   1
        #                   / \
        #                  2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = sol.preorderTraversal(root)
        self.assertEqual(result, [1, 2, 3])

    def test_preorderTraversal_left_skewed_tree(self):
        sol = Solution()
        # Construct a tree:   1
        #                     /
        #                    2
        #                   /
        #                  3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        result = sol.preorderTraversal(root)
        self.assertEqual(result, [1, 2, 3])

    def test_preorderTraversal_right_skewed_tree(self):
        sol = Solution()
        # Construct a tree:   1
        #                       \
        #                        2
        #                         \
        #                          3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        result = sol.preorderTraversal(root)
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    # 测试用例代码有问题
    unittest.main()
