"""
@Author : SakuraFox
@Time: 2024-12-05 19:24
@File : review44.py
@Description : 150. 逆波兰表达式求值-R1
逆波兰表达式求值思路：若为数字则压入栈；若为符号，取栈顶两个数
注意：
1.取栈顶两个数时，最底下的元素在符号左边([13,5]--->13/5)
2.符号对应的自定义计算方式
其他：整数除法的向零取整方式int(x / y) if x * y > 0 else -(abs(x) // abs(y))
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackList = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y) if x * y > 0 else -(abs(x) // abs(y))
        }

        for num in tokens:
            if num not in operators.keys():
                stackList.append(num)
            else:
                low = stackList.pop()
                up = stackList.pop()
                symbolTemp = operators[num]
                stackList.append(symbolTemp(int(up), int(low)))
        return stackList.pop()


Solution().evalRPN(["4","13","5","/","+"])
