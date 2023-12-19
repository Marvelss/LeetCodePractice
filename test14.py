# 字符串-替换空格
class Solution:
    def replaceSpace(self, s: str) -> str:
        s.replace()
        res = []
        for i in range(len(s)):
            if s[i] == '.':
                res.append(' ')
            else:
                res.append(s[i])

        return ''.join(res)

