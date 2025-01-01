"""
@Author : SakuraFox
@Time: 2025-01-01 21:02
@File : review62.py
@Description : 113. 路径总和 II

思路：代码与112. 路径总和类似，在其基础上，保存了路径元素
注意：resultT.append(list(subResultT))而不是
resultT.append(subResultT)，resultT会随着subResultT变化而变化，因为存储了 subResultT 的引用，

"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    targetSumA = 0

    def traverse(self, node: Optional[TreeNode], sumTemp: int, subResultT: List[List[int]],resultT:  List[List[int]]):
        subResultT.append(node.val)

        if not node.left and not node.right:
            if sumTemp == self.targetSumA:
                # print('a')
                # print(subResultT)
                resultT.append(list(subResultT))
                # print(resultT)
                return
        # print('=====外部-------')
        # print(resultT)
        if node.left:
            sumTemp += node.left.val
            # print(subResultT)
            self.traverse(node.left, sumTemp,subResultT, resultT)
            sumTemp -= node.left.val
            subResultT.pop()
        if node.right:
            sumTemp += node.right.val
            # print(subResultT)
            self.traverse(node.right, sumTemp,subResultT, resultT)
            sumTemp -= node.right.val
            subResultT.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.targetSumA = targetSum
        subResult = []
        result = []
        self.traverse(root, root.val, subResult,result)
        return result