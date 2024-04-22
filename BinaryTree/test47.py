"""
@Author : SakuraFox
@Time: 2024-04-22 20:32
@File : test47.py
@Description : 236. 二叉树的最近公共祖先(代码抄了一遍)
思路:从下至上遍历-->回溯-->后序遍历-->判断返回值结果得到最终解
重点:回溯的过程，以及结果是如何一层一层传上去的
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == q or root == p or not root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left and right:
            return right
        elif left and not right:
            return left
        else:
            return None
