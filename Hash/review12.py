"""
@Author : SakuraFox
@Time: 2024-07-09 18:53
@File : review12.py
@Description : 242.有效的字母异位词-review*-1(完美通过)
思路:表对应
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tableResult = [0] * 26
        for num in s:
            tableResult[ord('z') - ord(num)] += 1
        for num in t:
            tableResult[ord('z') - ord(num)] -= 1
        for num in tableResult:
            if num != 0:
                return False
        return True


print([0] * 26)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# 示例数据
actual = np.random.uniform(0, 100, 50)
predicted = actual + np.random.normal(0, 10, 50)

# 计算R^2
r2 = r2_score(actual, predicted)

# 创建图形
plt.figure(figsize=(6, 4))
plt.scatter(actual, predicted, c='black')
plt.plot([0, 100], [0, 100], 'r--')
plt.text(5, 90, f'$R^2 = {r2:.2f}$', fontsize=12)
plt.xlabel('实际病株率峰值(%)')
plt.ylabel('预测病株率峰值(%)')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
