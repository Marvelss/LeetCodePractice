"""
@Author : SakuraFox
@Time: 2024-12-25 13:49
@File : review55.py
@Description : 111. 二叉树的最小深度-R1

思路1：迭代法：
关键点：左右孩子都为空时为最低点，if not topE.left and not topE.right:return result

思路2：递归法
关键点：处理左右孩子不为空的逻辑
情况1：左空，右不空，右深度+1
情况2：左不空，右空，左深度+1
情况3：左不空，右不空，左右最小深度+1

"""
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        queue = collections.deque([node])
        result = 0
        while queue:
            result += 1
            for _ in range(len(queue)):
                topE = queue.popleft()
                if topE.left:
                    queue.append(topE.left)
                if topE.right:
                    queue.append(topE.right)
                if not topE.left and not topE.right:
                    return result
        return result

    def minDepth1(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftD = self.minDepth1(node.left)
        rightD = self.minDepth1(node.right)
        if node.left is None and node.right is not None:
            return rightD + 1
        if node.left is not None and node.right is None:
            return leftD + 1
        return min(leftD, rightD) + 1
