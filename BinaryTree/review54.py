"""
@Author : SakuraFox
@Time: 2024-12-24 18:41
@File : review54.py
@Description : 104. 二叉树的最大深度

思路1:层序遍历(迭代法)
优化点：tempL = []直接转为求深度
思路2:后续遍历(递归法)
左、右节点遍历到底，求max()并+1
"""
import collections
from typing import Optional

"""
class Solution:
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        ld = self.getDepth(node.left)
        rd = self.getDepth(node.right)
        depth = 1 + max(ld, rd)
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        resultList = []
        while queue:
            tempL = []
            for _ in range(len(queue)):
                topE = queue.popleft()
                tempL.append(topE)
                if topE.left:
                    queue.append(topE.left)
                if topE.right:
                    queue.append(topE.right)
            resultList.append(tempL)
        return len(resultList)

    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        leftL = self.getDepth(node.left)
        rightL = self.getDepth(node.right)
        return max(leftL,rightL)+1

    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
