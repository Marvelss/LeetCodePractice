"""
@Author : SakuraFox
@Time: 2024-04-18 19:34
@File : test46.py
@Description : 501. 二叉搜索树中的众数
方法1:遍历二叉树,并记录频率和对应数字到字典,获取最大频率
方法2:利用二叉树性质(跟着代码抄了一遍)
核心为3个点
1:首先使用pre记录上一个子节点
2:elif self.pre.val == cur.val:  # 与前一个节点相同+1有效计数
3:若相等则添加进结果,若大则替换最大频率,并删除原结果
if self.count == self.maxCount:
  self.result.append(cur.val)
if self.count > self.maxCount:
 self.maxCount = self.count
 self.result = [cur.val]  # 清空上一个最大频率的计数
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxCount = 0  # 最大频率
        self.count = 0  # 频率
        self.pre = None
        self.result = []

    def searchBTS(self, cur):
        if not cur:
            return
        self.searchBTS(cur.left)

        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:  # 与前一个节点相同+1有效计数
            self.count += 1
        else:
            self.count = 1
        self.pre = cur

        if self.count == self.maxCount:
            self.result.append(cur.val)
        if self.count > self.maxCount:
            self.maxCount = self.count
            self.result = [cur.val]  # 清空上一个最大频率的计数
        self.searchBTS(cur.right)
        return

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.searchBTS(root)

        return self.result
