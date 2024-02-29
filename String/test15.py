# 151.翻转字符串里的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)

s = Solution().reverseWords("  hello world!  ")
print(s)