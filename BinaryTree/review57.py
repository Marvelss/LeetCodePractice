"""
@Author : SakuraFox
@Time: 2024-12-25 14:09
@File : review57.py
@Description : 110. 平衡二叉树（思路抄）

思路1（不可行）:判断左右两侧节点深度，无法解决[1,2,3,4,5,6,null,8]情况

思路2：递归法（后序遍历），基于基础遍历模板改版，改动出：第一步给出返回值
1.函数及返回值：若左右节点高度不一致返回-1
2.终止条件：与平常一样
3.单层逻辑：左节点、右节点、中节点：abs(left_height - right_height) > 1

"""
from typing import Optional

"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countHeight(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        leftH = self.countHeight(node.left)
        if leftH == -1:
            return -1
        rightH = self.countHeight(node.right)
        if rightH == -1:
            return -1

        if abs(leftH - rightH) > 1:
            return -1
        else:
            return max(leftH, rightH) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.countHeight(root) != -1:
            return True
        else:
            return False
