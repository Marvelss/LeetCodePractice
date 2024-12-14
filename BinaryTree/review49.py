"""
@Author : SakuraFox
@Time: 2024-12-14 9:44
@File : review49.py
@Description : 94. 二叉树的中序遍历-R1
思路：
1.参数和返回值
2.终止条件
3.单层逻辑
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, nodeT, resultList):
        if nodeT is None:
            return None
        self.traverse(nodeT.left, resultList)
        resultList.append(nodeT.val)
        self.traverse(nodeT.right, resultList)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
