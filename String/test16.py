# 字符串-剑指Offer58-II.左旋转字符串
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        pwd_list = list(password)
        s1, e1 = 0, target - 1
        s2, e2 = target, len(pwd_list) - 1
        s3, e3 = 0, len(pwd_list) - 1
        while s1 < e1:
            temp = pwd_list[s1]
            pwd_list[s1] = pwd_list[e1]
            pwd_list[e1] = temp
            s1 += 1
            e1 -= 1
        while s2 < e2:
            temp = pwd_list[s2]
            pwd_list[s2] = pwd_list[e2]
            pwd_list[e2] = temp
            s2 += 1
            e2 -= 1
        while s3 < e3:
            temp = pwd_list[s3]
            pwd_list[s3] = pwd_list[e3]
            pwd_list[e3] = temp
            s3 += 1
            e3 -= 1
        return ''.join(pwd_list)


print(Solution().dynamicPassword('abcdef', 3))
