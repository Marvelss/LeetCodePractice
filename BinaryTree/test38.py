"""
@Author : SakuraFox
@Time: 2024-03-26 19:13
@File : test38.py
@Description: 513.找树左下角的值
疑惑：为什么获取最大深度需要回溯？
A:（同一深度会出现其他叶子节点，而题目要求最左边）
对上述A的A：
上述回答不对，获取最左边节点由if depth > self.maxDepth控制
其他：使用断点逐一观测node、depth变化明晰许多

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    def findBottomLeftValue(self, root: Optional[TreeNode]):
        if not root.left and not root.right:
            return root.val
        self.traversal(root, 0)
        return self.result, self.maxDepth


node1 = TreeNode(1, TreeNode(4))
node2 = TreeNode(3, TreeNode(7), TreeNode(5))
root = TreeNode(2, node1, node2)
print(Solution().findBottomLeftValue(root))
