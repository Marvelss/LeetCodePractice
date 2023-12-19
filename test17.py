# 卡码网题目右旋字符串

class Solution:
    def reverseWords(self, s: str, num: int) -> str:
        list1 = list(s)
        print(list1)
        i = 0
        j = len(list1) - 1
        self.reverse_word(list1, i, j)
        print(list1)
        s1_s = 0
        s1_e = num - 1
        s2_s = num
        s2_e = len(list1) - 1
        self.reverse_word(list1, s1_s, s1_e)
        self.reverse_word(list1, s2_s, s2_e)
        return ''.join(list1)

    def reverse_word(self, list1, i, j):
        while i <= j:
            list1[i], list1[j] = list1[j], list1[i]
            j -= 1
            i += 1
        return list1


print(Solution().reverseWords('abcdefg', 2))
