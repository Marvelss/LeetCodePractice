"""
@Author : SakuraFox
@Time: 2024-07-09 18:53
@File : review12.py
@Description : 242.有效的字母异位词-review*-1(完美通过)
思路:表对应
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tableResult = [0] * 26
        for num in s:
            tableResult[ord('z') - ord(num)] += 1
        for num in t:
            tableResult[ord('z') - ord(num)] -= 1
        for num in tableResult:
            if num != 0:
                return False
        return True


print([0] * 26)
