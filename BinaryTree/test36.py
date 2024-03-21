"""
@Author : SakuraFox
@Time: 2024-03-21 20:25
@File : test36.py
@Description: 257. 二叉树的所有路径
照着代码抄并理解了一遍
在前序遍历的基础上添加元素并多一步回溯操作
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self,
                  cur: Optional[TreeNode],
                  path: List[str],
                  result: List[str]):
        path.append(str(cur.val))
        if not cur.left and not cur.right:  # 到达叶子节点(无孩子)
            spath = '->'.join(map(str, path))
            result.append(spath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()  # 回溯
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result, path = [], []
        if not result:
            return result
        self.traversal(root, path, result)
        return result
