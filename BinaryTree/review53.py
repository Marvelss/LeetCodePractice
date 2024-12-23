"""
@Author : SakuraFox
@Time: 2024-12-23 15:17
@File : review53.py
@Description : 101. 对称二叉树（思路抄）

尝试思路1(有一种情况无法解决):
采用层序遍历，根据每层的数组镜像对称判断，但无法判断[1,2,2,null,3,null,3]的情况：左1空，左2=3，右1空，右2=3

思路：
1.递归函数：bool compare(TreeNode* left, TreeNode* right)
2.终止条件：①节点为空②节点不空，数值不等
3.单层循环：节点不空，数值相等（外侧、内侧）

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compare(self, left, right):
        # 节点为空
        if left is None and right is None:
            return True
        elif left is not None and right:
            return False
        elif left and right is not None:
            return False
        # 节点不为空，数值不等
        elif left.val != right.val:
            return False
        isOutside = self.compare(left.left, right.right)
        isInside = self.compare(left.right, right.left)
        isS = isInside and isOutside

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 遍历左右节点如果不相等返回False
        if not root:
            return True
        return self.compare(root.left, root.right)
