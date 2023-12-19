from typing import List


# 字符串-反转字符串


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        while i <= j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return s

s = Solution()
res = s.reverseString(['h', 'e', 'l', 'l', 'o'])
print(res)


# 数组-最大学生房间
