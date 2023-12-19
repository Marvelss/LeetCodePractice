class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = 0
        sum = 0
        l = len(nums)
        left = 0
        right = 0
        r = float('inf')
        while right < l:
            sum += nums[right]
            while sum >= target:
                r = min(r, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return r if r != float('inf') else 0


if __name__ == '__main__':
    s = Solution()
    target = 5
    nums = [1, 2, 3, 4, 7, 9]
    print(s.minSubArrayLen(target, nums))
