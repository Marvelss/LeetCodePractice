"""
@Author : SakuraFox
@Time: 2024-12-02 20:20
@File : review42.py
@Description : 20. 有效的括号-R1
思路：
问题出现情况：
1.左边符合多余和右边符合多余
2.左右符合不多余，但不匹配

方法1（左括号先入栈）：俄罗斯方块
1.若栈内无元素则添加，元素则进行消除
2.取栈顶元素，若和遍历的元素相对应便消除，否则元素入栈

方法2（右括号先入栈）：
1.遍历字符串匹配的过程中，发现栈里没有要匹配的字符则return false
2.若栈为空，则左右无多余
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stackList = []
        for num in s:
            if num == '(':
                stackList.append(')')
            elif num == '{':
                stackList.append('}')
            elif num == '[':
                stackList.append(']')
            # 若没遍历完就栈为空，或栈顶元素与当前元素不匹配，则说明False
            elif not stackList or stackList[-1] != num:
                return False
            else:
                stackList.pop()
        return len(stackList) == 0


print(Solution().isValid("(]"))
