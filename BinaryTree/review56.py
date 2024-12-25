"""
@Author : SakuraFox
@Time: 2024-12-25 10:34
@File : review56.py
@Description : 222. 完全二叉树的节点个数-R1

思路1：通用法
1+self.countNodes(root.left)+self.countNodes(root.right)

思路2：根据完全二叉树性质，公式法
情况1：满二叉树（公式：节点数=2的深度次幂-1）
情况2：不是满二叉树（使用通用法）
注意:2 << leftD等于2 * 2的深度次幂，也可以直接改为2** leftD

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countT(self, nodeT: Optional[TreeNode]) -> int:
        if nodeT is None:
            return 0
        lC = self.countT(nodeT.left)
        rC = self.countT(nodeT.right)
        return lC + rC + 1

    def countNodes(self, node: Optional[TreeNode]) -> int:
        return self.countT(node)

    def countNodes1(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = node.left
        right = node.right
        leftD, rightD = 0, 0
        while left:
            left = left.left
            leftD += 1
        while right:
            right = right.right
            rightD += 1
        if leftD==rightD:
            return (2 << leftD) - 1
        return 1+self.countNodes(node.left)+self.countNodes(node.right)