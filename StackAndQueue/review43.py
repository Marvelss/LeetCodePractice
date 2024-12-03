"""
@Author : SakuraFox
@Time: 2024-12-03 19:13
@File : review43.py
@Description : 1047. 删除字符串中的所有相邻重复项
思路：与20. 有效的括号（左括号先入栈）一致，俄罗斯方块
优化代码：if result and result[-1] == elem:
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        resultStack = []
        for word in s:
            if len(resultStack):
                topWord = resultStack[-1]
                if topWord == word:
                    resultStack.pop()
                else:
                    resultStack.append(word)
            else:
                resultStack.append(word)
        return ''.join(resultStack)

    def removeDuplicates1(self, s: str) -> str:
        """
        优化后代码
        :param s:
        :return:
        """
        result = list()
        for elem in s:
            if result and result[-1] == elem:
                result.pop()
            else:
                result.append(elem)
        return ''.join(result)
