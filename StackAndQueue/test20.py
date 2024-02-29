"""
@Author  : SakuraFox
@Time    : 2023-12-21 9:14
@File    : test20.py
@Description : 20. 有效的括号
注意:从反面角度考虑不是有括号的两种情况,
[不匹配,多余(中途多余和最后一个元素多余)]去判断,
其他操作就是添加和弹出首部元素
"""

import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if len(stack) == 0 else False


class TestIsValid(unittest.TestCase):

    def test_valid_parentheses(self):
        s = "()"
        result = Solution().isValid(s)
        self.assertTrue(result)

    def test_valid_brackets(self):
        s = "[]"
        result = Solution().isValid(s)
        self.assertTrue(result)

    def test_valid_curly_braces(self):
        s = "{}"
        result = Solution().isValid(s)
        self.assertTrue(result)

    def test_valid_mixed_parentheses(self):
        s = "()[{}]"
        result = Solution().isValid(s)
        self.assertTrue(result)

    def test_invalid_parentheses(self):
        s = "(]"
        result = Solution().isValid(s)
        self.assertFalse(result)

    def test_invalid_brackets(self):
        s = "[)"
        result = Solution().isValid(s)
        self.assertFalse(result)

    def test_invalid_curly_braces(self):
        s = "{]"
        result = Solution().isValid(s)
        self.assertFalse(result)

    def test_invalid_mixed_parentheses(self):
        s = "([)]"
        result = Solution().isValid(s)
        self.assertFalse(result)


if __name__ == "__main__":
    # unittest.main()
    s = "[)"
    result = Solution().isValid(s)
