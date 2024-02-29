"""
@Author  : SakuraFox
@Time    : 2023-12-21 9:14
@File    : test20.py
@Description : 1047. 删除字符串中的所有相邻重复项
与20. 有效的括号类似,甚至与哈希表中的242.有效的字母异位词思想类似.
都是采取匹配抵消的思想,其中每次取result[-1](栈的末尾钚元素)与字符串一一匹配,
从而使得领近的元素也能迭代匹配到,类似于消消乐.

"""

import unittest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = list()
        for elem in s:
            if result and result[-1] == elem:
                result.pop()
            else:
                result.append(elem)
        return ''.join(result)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_removeDuplicates1(self):
        self.assertEqual(self.solution.removeDuplicates("azxxzy"), "ay")

    def test_removeDuplicates2(self):
        self.assertEqual(self.solution.removeDuplicates("abbaca"), "ca")


if __name__ == "__main__":
    unittest.main()
