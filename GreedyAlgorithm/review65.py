"""
@Author : SakuraFox
@Time: 2025-01-06 13:09
@File : review65.py
@Description : 455. 分发饼干-R1

思路1：双层for循环（超出时间限制）
1.从大到小排序g
2.遍历s，若尺寸大于胃口，结果+1，且在g中移除该元素

思路2：g从大到小排序，s从小到大排序，g与s相减，判断大于0的元素个数（不行，最大尺寸匹配较小胃口）
问题：最大尺寸匹配较小胃口，应该是最大尺寸匹配最大胃口
用例：g=[10,9,8,7]；s=[5,6,7,8]解决不了

思路3：单层for循环(最大尺寸匹配最大胃口)
关键点：使用尺寸中的下标自减

"""
from typing import List

"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count, index = 0, len(s) - 1
        g.sort()
        s.sort()

        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                count += 1
                index -= 1
        return count
"""


class Solution:
    def findContentChildren3(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        j = len(s) - 1
        res = 0
        for i in range(len(g) - 1, -1, -1):
            if j >= 0 and s[j] >= g[i]:
                res += 1
                j -= 1
        return res

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        # 计算需要填充的长度
        result = []
        fill_length = len(g) - len(s)
        if fill_length < 0:
            g.extend([2 ** 31] * abs(fill_length))
        else:
            # 用 0 填充 s
            s.extend([0] * fill_length)
        g.sort(reverse=True)
        s.sort()

        for i in range(len(s)):
            result.append(s[i] - g[i])
        return sum(1 for x in result if x > 0)

    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort(reverse=True)
        print(g)
        if not len(s):
            return 0
        for num in s:
            for i in g:
                if i <= num:
                    res += 1
                    g.remove(i)
                    break
        return res
