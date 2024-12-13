"""
@Author : SakuraFox
@Time: 2024-12-12 19:47
@File : review47.py
@Description : 144. 二叉树的前序遍历-R1
思路：递归三步走
1.确定参数、返回值
2.确定终止条件
3.确定单层处理逻辑

卡点：
1.若cur为null则对其进行处理，否则会出现val
2.递归时不需要while循环，会陷入循环
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, cur: Optional[TreeNode], listT: List[int]):
        if cur is None:
            return None
        listT.append(cur.val)
        self.traverse(cur.left, listT)
        self.traverse(cur.right, listT)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        result = []
        while cur:
            result.append(cur.val)
            self.traverse(cur.left, result)
            self.traverse(cur.right, result)
        self.traverse(cur, result)
        return result


Solution.preorderTraversal([1, 'null', 2, 3])
