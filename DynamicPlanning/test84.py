"""
@Author : SakuraFox
@Time: 2024-10-16 21:08
@File : test84.py
@Description : 139.单词拆分

要点：
1.目标字符串的子字符串在wordDict中存在单词-->s[j:i] in wordDict
2.强调顺序-->组合-->先遍历背包
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[len(s)]
