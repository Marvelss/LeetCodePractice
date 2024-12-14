"""
@Author : SakuraFox
@Time: 2024-12-13 20:28
@File : review48.py
@Description : 145. 二叉树的后序遍历-R1
"""


# 迭代法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, listNode, valueList):
        if listNode is None:
            return None
        self.traverse(listNode.left, valueList)
        self.traverse(listNode.right, valueList)
        valueList.append(listNode.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
