"""
@Author : SakuraFox
@Time: 2024-11-27 13:49
@File : review38.py
@Description : 28. 找出字符串中第一个匹配项的下标(抄)
思路：KMP算法
1.初始化与意义i：后缀末尾,j：子串的最长相等前后缀的长度,nextT：最长相等前后缀的长度
2.处理前后缀不相同情况
3.处理前后缀相同情况
4.获得next数值
"""


class Solution:
    def startKMP(self, nextT, s):
        # 初始化 i, j, next1
        # 处理前后缀不相同情况
        # 处理前后缀相同情况
        # 获得next下标
        j = 0
        nextT[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:  # 前后缀不同
                j = nextT[j - 1]  # 一直回退
            if s[i] == s[j]:  # 相同前后缀
                print(s[i])
                print(i)
                j += 1  # 最长相同前后缀+1
                nextT[i] = j  # 赋值
            print(nextT)

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        nextT1 = [0] * len(needle)
        self.startKMP(nextT1, needle)
        print(nextT1)

        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nextT1[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


Solution().strStr("mississippi", "issip")
