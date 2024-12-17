"""
@Author : SakuraFox
@Time: 2024-12-17 14:45
@File : review51.py
@Description : 102. 二叉树的层序遍历-R1(部分思路自己写)
思路：
1使用队列，将每一层节点放入队列进行遍历

注意:
1.队列的popleft()是左边头部出口，pop()是右边尾部进口

卡点：
1.for _ in range(len(queue)):代表处理一层节点

"""
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                rootNode = queue.popleft()
                temp.append(rootNode.val)
                leftNode = rootNode.left
                rightNode = rootNode.right
                if leftNode:
                    queue.append(leftNode)
                if rightNode:
                    queue.append(rightNode)
            result.append(temp)
        return result
