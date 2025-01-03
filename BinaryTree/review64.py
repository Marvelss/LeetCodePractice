"""
@Author : SakuraFox
@Time: 2025-01-03 9:27
@File : review64.py
@Description : 654. 最大二叉树(一次过，牛牛牛)
1.nums，节点
2.终止条件：数组为空
3.单层逻辑
①取最大值作为切割点
②左右数组作为左右节点带入递归
"""
from typing import List, Optional

"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return TreeNode()
        max_value = 0
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
        root = TreeNode(val=max_value)
        rootIds = nums.index(max_value)
        if rootIds > 0:
            leftList = nums[:rootIds]
            root.left = self.constructMaximumBinaryTree(leftList)

        if rootIds < len(nums) - 1:
            rightList = nums[rootIds + 1:]
            root.right = self.constructMaximumBinaryTree(rightList)
        return root

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return
        rootNode = TreeNode(val=max(nums))
        if len(nums) == 1:
            return rootNode
        index = nums.index(rootNode.val)
        leftNums, rightNums = nums[:index], nums[index + 1:]
        rootNode.left = self.constructMaximumBinaryTree(leftNums)
        rootNode.right = self.constructMaximumBinaryTree(rightNums)
        return rootNode
