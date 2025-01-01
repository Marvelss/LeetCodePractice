"""
@Author : SakuraFox
@Time: 2025-01-01 19:54
@File : review61.py
@Description : 112. 路径总和

思路1：递归法（先序遍历）
1.节点、当前和值、是否存在路径
2.左、右节点不存在，且当前和值等于目标值，则添加一个可能的路径
3.累加当前节点值，回溯
"""

"""
class Solution:
    def traversal(self, node, count):
        if not node.left and not node.right and count == 0:
            return True
        if not node.left and not node.right:
            return False
        if node.left:
            count -= node.left.val
            if self.traversal(node.left, count):
                return True
            count += node.left.val

        if node.right:
            count -= node.right.val
            if self.traversal(node.right, count):
                return True
            count += node.right.val
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.traversal(root, targetSum-root.val)

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    targetSumA = 0

    def traverse(self, node: Optional[TreeNode], sumTemp, resultT):
        if not node.left and not node.right:
            if sumTemp == self.targetSumA:
                resultT.append(1)
                return
            else:
                resultT.append(0)
                return

        if node.left:
            sumTemp += node.left.val
            self.traverse(node.left, sumTemp, resultT)
            sumTemp -= node.left.val
        if node.right:
            sumTemp += node.right.val
            self.traverse(node.right, sumTemp, resultT)
            sumTemp -= node.right.val

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.targetSumA = targetSum
        result = []
        self.traverse(root, 0, result)
        if 1 in result:
            return True
        else:
            return False
