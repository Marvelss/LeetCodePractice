# hash table
# 242.有效的字母异位词

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in t:
            record[ord(i) - ord("a")] += 1
        for j in s:
            record[ord(j) - ord("a")] -=1
        for i in range(len(record)):
            if record[i] != 0:
                return False
        return True
