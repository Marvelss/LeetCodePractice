"""
@Author : SakuraFox
@Time: 2024-12-14 10:24
@File : review50.py
@Description : 144. 二叉树的前序遍历-R2
思路：迭代法-栈
先将根节点压入栈，然后压入右节点，左节点

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stackT = [root]
        result = []
        while not stackT:
            rootNode = stackT.pop()
            result.append(rootNode.val)
            if rootNode.right:
                stackT.append(rootNode.right)
            if rootNode.left:
                stackT.append(rootNode.left)
        return result
