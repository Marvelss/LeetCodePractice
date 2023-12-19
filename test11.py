# 第202题. 快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            if n in res:
                return False
            else:
                res.add(n)

    # 获取各个位上的数
    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
            print(n,r)
        return new_num


solution = Solution()
result = solution.get_sum(12345)
print(result)