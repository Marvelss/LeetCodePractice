"""
@Author  : SakuraFox
@Time    : 2024-01-04 22:41
@File    : test27.py
@Description : 94.二叉树的中序遍历(迭代法)
还不太明白
步骤:
1.遍历左边到根节点
2.按照中、右的顺序获取结果
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack_temp = []
        result = []
        cur = root
        while cur or stack_temp:
            # 访问左节点到底
            if cur:
                stack_temp.append(cur)
                cur = cur.left
            else:
                cur = stack_temp.pop()
                result.append(cur.val)
                cur = cur.right
        return result
