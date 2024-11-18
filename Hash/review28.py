"""
@Author : SakuraFox
@Time: 2024-11-18 9:55
@File : review28.py
@Description : 242.有效的字母异位词-r2
字符串转ASCII码使用函数ord()
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = [0] * 26
        for i in range(len(s)):
            result[ord(s[i]) - ord('a')] += 1
        for j in range(len(t)):
            result[ord(t[j]) - ord('a')] -= 1
        for num in result:
            if num != 0:
                return False
        return True
