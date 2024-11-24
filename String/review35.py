"""
@Author : SakuraFox
@Time: 2024-11-24 14:11
@File : review35.py
@Description : 344. 反转字符串-R2
思路：双指针法，left为0，right为len(字符串长度)-1，调换位置以实现反转
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while right > left:
            t = s[left]
            s[left] = s[right]
            s[right] = t
            left += 1
            right -= 1
