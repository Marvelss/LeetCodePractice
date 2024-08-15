"""
@Author : SakuraFox
@Time: 2024-08-15 18:49
@File : test67.py
@Description : 738. 单调递增的数字(思路抄)
思路:
1.位数小的地方-1,位数大的变为9(注意该位后所有都变为9)
2.从后往前遍历
注意:
1.字符串数字(正整数)比大小与数值一样:'9'>'8'
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strList = list(str(n))
        for i in range(len(strList) - 1, 0, -1):
            if strList[i] <= strList[i - 1]:
                strList[i - 1] = str(int(strList[i - 1]) - 1)
                strList[i] = 9
                # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
                for j in range(i, len(strList)):
                    strList[j] = '9'
        return int(''.join(strList))


print(Solution().monotoneIncreasingDigits(332))
