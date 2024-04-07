"""
@Author : SakuraFox
@Time: 2024-03-28 22:14
@File : test40.py
@Description : 617. 从中序与后序遍历序列构造二叉树(抄了一遍代码)
第一步：如果数组大小为零的话，说明是空节点了。
第二步：如果不为空，那么取后序数组最后一个元素作为节点元素。
第三步：找到后序数组最后一个元素在中序数组的位置，作为切割点
第四步：切割中序数组，切成中序左数组和中序右数组 （顺序别搞反了，一定是先切中序数组）
第五步：切割后序数组，切成后序左数组和后序右数组
第六步：递归处理左区间和右区间
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        splitIdx = inorder.index(rootVal)
        leftI = inorder[:splitIdx]
        rightI = inorder[splitIdx + 1:]
        leftP = postorder[:len(leftI)]
        rightP = postorder[len(leftI):len(postorder) - 1]
        root.left = self.buildTree(leftI, leftP)
        root.right = self.buildTree(rightI, rightP)
        return root
