"""
@Author : SakuraFox
@Time: 2024-12-26 15:01
@File : review58.py
@Description : 257. 二叉树的所有路径


思路：递归法-在原有递归遍历基础上扩展以下内容
1.初始化函数：传入path和result参数
2.终止添加：左右节点空
3.单层循环：中节点，添加->处理转换路径；左和右节点添加path.pop()作为回溯

注意：
if not cur.left and not cur.right: 等价于 if cur.left is None and cur.right is None:
"""
from typing import Optional, List

"""
class Solution:
    def traversal(self,
                  cur: Optional[TreeNode],
                  path: List[str],
                  result: List[str]):
        path.append(cur.val)
        if not cur.left and not cur.right:
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
        if not root:
            return result
        self.traversal(root, path, result)
        return result

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, cur, pathT, resultT):
        pathT.append(cur.val)
        if cur.left is None and cur.right is None:
            pathS = '->'.join(map(str, pathT))
            resultT.append(pathS)
            return
        if cur.left:
            self.traverse(cur.left, pathT, resultT)
            pathT.pop()
        if cur.right:
            self.traverse(cur.right, pathT, resultT)
            pathT.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        path, result = [], []
        self.traverse(root, path, result)
        return result
