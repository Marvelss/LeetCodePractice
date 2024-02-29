"""
@Author  : SakuraFox
@Time    : 2024-01-01 19:15
@File    : test22.py
@Description : 150. 逆波兰表达式求值
在<1047. 删除字符串中的所有相邻重复项>题目的基础上,
将判断是否匹配(相等)的操作转换成运算符的计算,
当遇到运算符时,弹出栈顶2个元素,并进行运算,将结果压入栈中,迭代循环.
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_in = []
        for elem in tokens:
            if elem not in {'+', '-', '*', '/'}:
                stack_in.append(elem)
            else:
                num1 = stack_in.pop()
                num2 = stack_in.pop()
                temp = self.calculate(int(num1), int(num2), elem)
                stack_in.append(temp)
        return int(stack_in.pop())

    def calculate(self, num1: int, num2: int, symbol) -> float:
        if symbol == '/':
            return num2 / num1
        if symbol == '*':
            return num2 * num1
        if symbol == '+':
            return num2 + num1
        if symbol == '-':
            return num2 - num1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_evalRPN(self):
        # Test case 1: Basic addition
        tokens1 = ["2", "3", "+"]
        self.assertEqual(self.solution.evalRPN(tokens1), 5)

        # Test case 2: Basic subtraction
        tokens2 = ["5", "2", "-"]
        self.assertEqual(self.solution.evalRPN(tokens2), 3)

        # Test case 3: Basic multiplication
        tokens3 = ["4", "6", "*"]
        self.assertEqual(self.solution.evalRPN(tokens3), 24)

        # Test case 4: Basic division
        tokens4 = ["8", "2", "/"]
        self.assertEqual(self.solution.evalRPN(tokens4), 4)

        # Test case 5: Complex expression
        tokens5 = ["10", "6", "9", "3", "/", "-", "*"]
        self.assertEqual(self.solution.evalRPN(tokens5), 30)
        tokens6 = ["18"]
        self.assertEqual(self.solution.evalRPN(tokens6), 18)
        # Add more test cases based on the specific requirements of your code


if __name__ == '__main__':
    unittest.main()
