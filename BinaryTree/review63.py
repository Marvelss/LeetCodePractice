"""
@Author : SakuraFox
@Time: 2025-01-02 16:06
@File : review63.py
@Description : 106.从中序与后序遍历序列构造二叉树、105. 从前序与中序遍历序列构造二叉树
106.从中序与后序遍历序列构造二叉树
思路：递归法
1.（中序数组，后序数组），节点
2.后序数组为空，则返回
3.
①找后序数组最后一个节点作为根节点，若后序数组长度为1，则返回节点
②以该根节点作为切割点，寻找对应中序遍历中的位置
③切中序数组
④根据中序数组中的左节点切后序数组
⑤递归左区间和右区间


105. 从前序与中序遍历序列构造二叉树
思路：基于中序与后序遍历序列构造二叉树，改动点：中序数组切割点，进而改变左右前序数组
注意点：
1.切分前/后序时，根据左中序的长度确定左前/序
2.遍历切割点时，若找到了，直接break，以节省时间
"""
from typing import List, Optional

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        splitIdx = inorder.index(rootVal)
        leftI, rightI = inorder[:splitIdx], inorder[splitIdx + 1:]
        leftP, rightP = postorder[:len(leftI)], postorder[len(leftI):len(postorder) - 1]
        root.left = self.buildTree(leftI, leftP)
        root.right = self.buildTree(rightI, rightP)
        return root
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not len(postorder):
            return
        rootNode = TreeNode(val=postorder[-1])
        if len(postorder) == 1:
            return rootNode
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == rootNode.val:
                index = i
                break
        leftInorder, rightInorder = inorder[:index], inorder[index + 1:len(inorder)]
        leftPostorder = postorder[:len(leftInorder)]

        tempPostorder = postorder
        # 排除leftInorder和根节点值
        for num in leftPostorder:
            tempPostorder.remove(num)
        tempPostorder.remove(rootNode.val)
        rightPostorder = tempPostorder
        rootNode.left = self.buildTree(leftInorder, leftPostorder)
        rootNode.right = self.buildTree(rightInorder, rightPostorder)
        return rootNode

    # 105.从前序与中序遍历序列构造二叉树
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not len(preorder):
            return
        rootNode = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return rootNode
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == rootNode.val:
                index = i
                break
        leftInorder, rightInorder = inorder[:index], inorder[index + 1:len(inorder)]
        # tempPreorder = preorder
        leftPreorder = preorder[1:index+1]
        rightPreorder = preorder[index+1:]
        # for num in leftInorder:
        #     tempPreorder.remove(num)
        # tempPreorder.remove(rootNode.val)
        # rightPreorder = tempPreorder
        rootNode.left = self.buildTree1(leftPreorder, leftInorder)
        rootNode.right = self.buildTree1(rightPreorder, rightInorder)
        return rootNode

