"""
@Author : SakuraFox
@Time: 2024-11-23 19:51
@File : review34.py
@Description : 383. 赎金信
思路：与242.有效的字母异位词思路一致，区别在最后判定条件
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = [0] * 26
        for word in magazine:
            res[ord('z') - ord(word)] += 1
        for word in ransomNote:
            res[ord('z') - ord(word)] -= 1
        for num in res:
            if num < 0:
                return False
        return True
