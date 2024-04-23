"""
@Author : SakuraFox
@Time: 2024-04-23 20:10
@File : test48.py
@Description : 235. 二叉搜索树的最近公共祖先(抄了一遍,)
根据二叉树性质,通过中节点 > p && 中节点> q 或者 中节点 < q && 中节点 < p判断
同时大于或同时小于p、q不太理解
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traversal(self, cur, p, q):
        if not cur:
            return cur
        if cur.val > p.val and cur.val > q.val:
            left = self.traversal(cur.left, p, q)
            if left:
                return left
        if cur.val < p.val and cur.val < q.val:
            right = self.traversal(cur.right, p, q)
            if right:
                return right
        return cur

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)
