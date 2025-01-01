"""
@Author : SakuraFox
@Time: 2025-01-01 14:38
@File : review60.py
@Description : 513. 找树左下角的值

思路1：迭代法（层序遍历）
取最后一层的第一个元素
思路2：递归法（先序遍历）
1.节点+深度
2.判断叶子节点，深度
3.深度+1，回溯

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
    maxDepth = 0
    result = 0

    def traversal(self, node, depth):
        if not node.left and not node.right:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.result = node.val
            return
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        self.traversal(root, 0)
        return self.result

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result, maxDepth = 0, 0

    def traverse(self, node: Optional[TreeNode], depthT: int):
        if not node.left and not node.right:
            if depthT > self.maxDepth:
                self.maxDepth = depthT
                self.result = node.val
                return
        if node.left:
            depthT += 1
            self.traverse(node.left, depthT)
            depthT -= 1
        if node.right:
            depthT += 1
            self.traverse(node.right, depthT)
            depthT -= 1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.traverse(root, self.maxDepth)
        return self.result

    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        result = root.val
        queue = collections.deque([root])
        while queue:
            tempResult = []
            for _ in range(len(queue)):
                topN = queue.popleft()
                tempResult.append(topN.val)

                if topN.left:
                    # tempResult.append(topN.left.val)
                    queue.append(topN.left)
                if topN.right:
                    queue.append(topN.right)
                    # tempResult.append(topN.right.val)
            # print(tempResult)
            # if len(tempResult):
            #     result = tempResult[0]
            result = tempResult[0]
        return result
