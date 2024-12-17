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

637.二叉树的层平均值
思路：基于上述模板加一步操作：取层平均值
107.二叉树的层序遍历II（倒叙元素）
思路：基于上述模板加一步操作：倒叙排列元素
小技巧：倒叙排列元素-a[::-1]替换for n in range(len(result) - 1, -1, -1)
199.二叉树的右视图
思路：基于上述模板加一步操作：取层末尾元素
515.在每个树行中找最大值
思路：基于上述模板加一步操作：取层最大值
429.N叉树的层序遍历
思路：基于上述模板加一步操作：遍历子孩子节点数组添加进队列
注意：子孩子节点是个数组
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

    # 637.二叉树的层平均值
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queen = collections.deque([root])
        result = []
        while queen:
            layerResult = []
            for _ in range(len(queen)):
                rootNode = queen.popleft()
                layerResult.append(rootNode.val)
                if rootNode.left:
                    queen.append(rootNode.left)
                if rootNode.right:
                    queen.append(rootNode.right)
            result.append(sum(layerResult) / len(layerResult))
        return result

    # 107.二叉树的层序遍历II（倒叙元素）
    class Solution:
        def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            queen = collections.deque([root])
            result, resultReverse = [], []
            while queen:
                layerResult = []
                for _ in range(len(queen)):
                    rootNode = queen.popleft()
                    layerResult.append(rootNode.val)
                    if rootNode.left:
                        queen.append(rootNode.left)
                    if rootNode.right:
                        queen.append(rootNode.right)
                result.append(layerResult)
            for n in range(len(result) - 1, -1, -1):
                resultReverse.append(result[n])
            return resultReverse

    # 199.二叉树的右视图
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queen = collections.deque([root])
        result = []
        while queen:
            layerResult = []
            for _ in range(len(queen)):
                rootNode = queen.popleft()
                layerResult.append(rootNode.val)
                if rootNode.left:
                    queen.append(rootNode.left)
                if rootNode.right:
                    queen.append(rootNode.right)
            result.append(layerResult[-1])
        return result

    # 515.在每个树行中找最大值
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queen = collections.deque([root])
        result = []
        while queen:
            layerResult = []
            for _ in range(len(queen)):
                rootNode = queen.popleft()
                layerResult.append(rootNode.val)
                if rootNode.left:
                    queen.append(rootNode.left)
                if rootNode.right:
                    queen.append(rootNode.right)
            result.append(max(layerResult))
        return result

    # 429.N叉树的层序遍历
    def levelOrderN(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queen = collections.deque([root])
        result = []
        while queen:
            layerResult = []
            for _ in range(len(queen)):
                rootNode = queen.popleft()
                layerResult.append(rootNode.val)
                if rootNode.children:
                    for i in range(len(rootNode.children)):
                        queen.append(rootNode.children[i])
            result.append(layerResult)
        return result