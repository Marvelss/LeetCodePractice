"""
@Author : SakuraFox
@Time: 2024-11-26 14:42
@File : review37.py
@Description : 151. 反转字符串中的单词
思路：
1.反转所有字母
2.去除多余空格(根据空格进行循环判断处理)
3.反转单词

注意：
1.先执行fast < len(s)
while s[fast] != " " and fast < len(s)和while fast < len(s) and s[fast] != " "
"""


class Solution:
    def reverseWords1(self, s: str) -> str:
        """
        方法一：根据空格分割，反转
        :param s:
        :return:
        """
        words = s.split()
        left, right = 0, len(words) - 1
        while right > left:
            t = words[left]
            words[left] = words[right]
            words[right] = t
            left += 1
            right -= 1
        return ''.join(words)

    # 反转所有字母
    def reverseWord(self, s, start, end):
        while start > end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        """
        方法一：1.反转所有字母
            2.去除多余空格(根据空格进行循环判断处理)
            3.反转单词
        :param s:
        :return:
        """
        result = ""
        fast = 0
        # 1. 首先将原字符串反转并且除掉空格, 并且加入到新的字符串当中
        # 由于Python字符串的不可变性，因此只能转换为列表进行处理
        s = list(s)
        s.reverse()
        while fast < len(s):
            if s[fast] != " ":
                if len(result) != 0:
                    result += " "
                while s[fast] != " " and fast < len(s):
                    result += s[fast]
                    fast += 1
            else:
                fast += 1
        # 将每个单词反转
        slow, fast = 0, 0
        result = list(result)
        while fast < len(result):
            if fast == len(result) or result[fast] == ' ':
                self.reverseWord(result, slow, fast - 1)
                slow = fast + 1
                fast += 1
            else:
                fast += 1
        return ''.join(s)
