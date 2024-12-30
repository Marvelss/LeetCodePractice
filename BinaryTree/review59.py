"""
@Author : SakuraFox
@Time: 2024-12-30 18:31
@File : review59.py
@Description : 404.左叶子之和-R1

思路1：迭代法(在子节点无左子树与右子树时求和)
注意：题目要求左叶子，只求无子节点的左子树，如[1,2,3,4,5]，不计算2这个左子树
if not topNode.left.left and not topNode.left.right:
    resSum += topNode.left.val

思路2：递归法
1.参数：节点，返回值：求和数组
2.if not node：return 0
3.在左子树是左叶子的情况下累加：
if root.left is not None and root.left.left is None and root.left.right is None:
    leftN = node.left.val
return leftN + rightN
或者另一种理解，对中节点做判断
if node.left and not node.left.left and not node.left.right:
    midValue = node.left.val
return leftN + rightN + midValue



"""
import collections
from typing import Optional

"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        left = self.sumOfLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right:
            left = root.left.val
        right = self.sumOfLeftLeaves(root.right)
        return left + right

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        resSum = 0
        while queue:
            for _ in range(len(queue)):
                topNode = queue.popleft()
                # print(topNode.val)
                if topNode.left:
                    queue.append(topNode.left)
                    # 求左叶子
                    if not topNode.left.left and not topNode.left.right:
                        resSum += topNode.left.val
                if topNode.right:
                    queue.append(topNode.right)
        return resSum

    def traverse(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        # 左
        leftN = self.traverse(node.left)
        if node.left and not node.left.left and not node.left.right:
            leftN = node.left.val
        # 右
        rightN = self.traverse(node.right)

        # 中：左子树的左节点+右子树的左节点
        return leftN + rightN

    def traverse1(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftN = self.traverse(node.left)
        rightN = self.traverse(node.right)
        midValue = 0
        if node.left and not node.left.left and not node.left.right:
            midValue = node.left.val

        return leftN + rightN + midValue

    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)
