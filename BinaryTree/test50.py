"""
@Author : SakuraFox
@Time: 2024-04-29 20:23
@File : test50.py
@Description : 450. 删除二叉搜索树中的节点(抄)
考虑删除节点的子节点5种情况:
1.无该删除节点
2.该删除节点子节点都为空
3.该删除节点左子树为空
4.该删除节点右子树为空
5.该删除节点子节点不为空(删除节点的左子树置于下次层左子树,同时右子树接在被删除节点)
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # 该情况较难理解
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
