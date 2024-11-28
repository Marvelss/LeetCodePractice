"""
@Author : SakuraFox
@Time: 2024-11-28 19:19
@File : review39.py
@Description : 28. 找出字符串中第一个匹配项的下标-R1
注意：匹配haystack和needl时，下标从0开始；KMP下标从1开始，因为next[0]=0
for i in range(len(haystack)):
"""


class Solution:
    def startKMP(self, sList, nextT):
        j = 0
        nextT[0] = 0
        for i in range(1, len(sList)):
            while j > 0 and sList[i] != sList[j]:
                j = nextT[j - 1]
            if sList[i] == sList[j]:
                j += 1
                nextT[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        nextTT = [0] * len(needle)
        self.startKMP(needle, nextTT)
        j = 0

        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nextTT[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                print(i)
                print(nextTT)
                print(i - len(needle) + 1)
                return i - len(needle) + 1
        return -1


Solution().strStr("sadbutsad", "sad")
