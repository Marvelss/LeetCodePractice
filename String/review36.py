"""
@Author : SakuraFox
@Time: 2024-11-25 18:04
@File : review36.py
@Description : 541. 反转字符串 II
方法一：
思路：
1.步长为2*k的for循环
2.截取字符串下标为(sList[preIndex:(k + i)]) 和 ''.join(sList[(k + i):(2 * k + i)])
3.前k个字符反转，后k个到2k个字符不处理
方法二：
思路：只处理需要反转的字符串的下标
"""


class Solution:
    def reverseSubStr(self, num: list) -> str:
        """
        反转子字符串
        :param num:
        :return:
        """
        left, right = 0, len(num) - 1
        while right > left:
            t = num[left]
            num[left] = num[right]
            num[right] = t
            right -= 1
            left += 1
        return ''.join(num)

    def reverseStr1(self, s: str, k: int) -> str:
        if len(s) == 1:
            return s
        sList = list(s)
        preIndex = 0
        subStr = ''
        i = 0
        while i <= len(sList) - 1:
            subStr = subStr + self.reverseSubStr(sList[preIndex:(k + i)]) + ''.join(sList[(k + i):(2 * k + i)])
            preIndex = (2 * k + i)
            i += 2 * k
        return subStr

    def reverseStr2(self, s: str, k: int) -> str:
        sList = list(s)
        for cur in range(0, len(sList), 2 * k):
            sList[cur:cur+k] = self.reverseSubStr(sList[cur:cur+k])
        return ''.join(sList)


